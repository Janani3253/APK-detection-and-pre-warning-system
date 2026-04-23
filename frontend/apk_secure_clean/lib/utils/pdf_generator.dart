import 'dart:io';
import 'package:path_provider/path_provider.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;

class PdfGenerator {
  static Future<File> generate(Map<String, dynamic> data) async {
    final pdf = pw.Document();

    final apk = data["apk_details"];
    final analysis = data["permission_analysis"];
    final sandbox = analysis["sandbox"];

    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        build: (context) => [
          pw.Center(
            child: pw.Text(
              "APK SECURITY REPORT",
              style: pw.TextStyle(
                  fontSize: 24,
                  fontWeight: pw.FontWeight.bold),
            ),
          ),

          pw.SizedBox(height: 20),

          header("Application Info"),
          row("App Name", apk["app_name"]),
          row("Package", apk["package_name"]),
          row("Version", apk["version_name"]),
          row("Category", data["app_category"]),
          row("Verdict", data["verdict"]),
          row("Risk Score", "${analysis["risk_score"]}%"),

          pw.SizedBox(height: 15),

          header("Dangerous Permissions"),
          bulletList(analysis["dangerous"]),

          pw.SizedBox(height: 15),

          header("Sandbox Result"),
          row("Installed", sandbox["installed"].toString()),
          row("Launched", sandbox["launched"].toString()),
          row("Crashed", sandbox["crashed"].toString()),
          row("Sandbox Score",
              "${sandbox["sandbox_score"]}%"),

          pw.SizedBox(height: 15),

          header("Warning"),
          pw.Text(data["warning"]),
        ],
      ),
    );

    final dir = await getApplicationDocumentsDirectory();
    final file = File(
        "${dir.path}/${apk["package_name"]}_report.pdf");

    await file.writeAsBytes(await pdf.save());
    return file;
  }

  static pw.Widget header(String text) {
    return pw.Padding(
      padding: const pw.EdgeInsets.only(bottom: 6),
      child: pw.Text(text,
          style: pw.TextStyle(
              fontSize: 18,
              fontWeight: pw.FontWeight.bold)),
    );
  }

  static pw.Widget row(String k, String v) {
    return pw.Padding(
      padding: const pw.EdgeInsets.symmetric(vertical: 2),
      child: pw.Row(
        mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
        children: [
          pw.Text(k),
          pw.Text(v),
        ],
      ),
    );
  }

  static pw.Widget bulletList(List list) {
    return pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: list
          .map<pw.Widget>(
              (e) => pw.Bullet(text: e.toString()))
          .toList(),
    );
  }
}