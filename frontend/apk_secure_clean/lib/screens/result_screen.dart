import 'dart:io';
import 'package:flutter/material.dart';
import 'package:printing/printing.dart';

import '../utils/pdf_generator.dart';
import '../utils/constants.dart';

class ResultScreen extends StatefulWidget {
  final Map<String, dynamic> result;

  const ResultScreen({super.key, required this.result});

  @override
  State<ResultScreen> createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> {
  bool generating = false;

  @override
  Widget build(BuildContext context) {
    final apk = widget.result["apk_details"];
    final verdict = widget.result["verdict"];
    final risk = widget.result["permission_analysis"]["risk_score"];

    return Scaffold(
      backgroundColor: AppConstants.bgColor,
      appBar: AppBar(
        title: const Text("Analysis Result"),
        backgroundColor: AppConstants.primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            infoCard("App Name", apk["app_name"]),
            infoCard("Package", apk["package_name"]),
            infoCard("Verdict", verdict),
            infoCard("Risk Score", "$risk %"),

            const Spacer(),

            SizedBox(
              width: double.infinity,
              height: 50,
              child: ElevatedButton.icon(
                icon: const Icon(Icons.picture_as_pdf),
                label: Text(generating
                    ? "Generating PDF..."
                    : "Download Security Report"),
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppConstants.primaryColor,
                ),
                onPressed: generating ? null : generatePdf,
              ),
            )
          ],
        ),
      ),
    );
  }

  Widget infoCard(String title, String value) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(title,
                style:
                const TextStyle(fontWeight: FontWeight.bold)),
            Flexible(child: Text(value)),
          ],
        ),
      ),
    );
  }

  Future<void> generatePdf() async {
    setState(() => generating = true);

    final File file =
    await PdfGenerator.generate(widget.result);

    await Printing.sharePdf(
      bytes: await file.readAsBytes(),
      filename: "apk_report.pdf",
    );

    setState(() => generating = false);
  }
}