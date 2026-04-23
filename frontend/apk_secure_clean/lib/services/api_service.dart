import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;
import '../utils/constants.dart';

class ApiService {
  /// Upload APK and receive analysis report
  static Future<Map<String, dynamic>> uploadApk(File apkFile) async {
    try {
      final uri = Uri.parse(
        AppConstants.baseUrl + AppConstants.uploadEndpoint,
      );

      final request = http.MultipartRequest('POST', uri);

      request.files.add(
        await http.MultipartFile.fromPath(
          'file',
          apkFile.path,
          filename: apkFile.path.split('/').last,
        ),
      );

      final streamedResponse = await request.send();
      final responseBody = await streamedResponse.stream.bytesToString();

      if (streamedResponse.statusCode == 200) {
        return jsonDecode(responseBody);
      } else {
        throw Exception(
          "Server Error (${streamedResponse.statusCode}): $responseBody",
        );
      }
    } catch (e) {
      throw Exception("API Error: $e");
    }
  }
}