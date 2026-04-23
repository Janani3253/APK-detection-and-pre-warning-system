import 'package:flutter/material.dart';

import '../widgets/permission_card.dart';
import '../widgets/risk_badge.dart';
import '../widgets/sandbox_card.dart';
import 'result_screen.dart';
import '../lang/lang.dart';

class AnalysisScreen extends StatelessWidget {
  final Map<String, dynamic> result;

  const AnalysisScreen({super.key, required this.result});

  @override
  Widget build(BuildContext context) {
    final permissions = result['permission_analysis'];
    final sandbox = permissions['sandbox'];

    return Scaffold(
      appBar: AppBar(
        title: Text(AppLang.instance.t('analysis_complete')),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            RiskBadge(
              risk: permissions['risk_score'],
              verdict: result['verdict'],
            ),

            const SizedBox(height: 20),

            PermissionCard(
              title: AppLang.instance.t('permissions'),
              permissions: List<String>.from(permissions['expected']),
              color: Colors.green,
            ),

            PermissionCard(
              title: AppLang.instance.t('acceptable_permissions'),
              permissions: List<String>.from(permissions['acceptable']),
              color: Colors.orange,
            ),

            PermissionCard(
              title: AppLang.instance.t('dangerous_permissions'),
              permissions: List<String>.from(permissions['dangerous']),
              color: Colors.red,
            ),

            const SizedBox(height: 20),

            SandboxCard(sandbox: sandbox),

            const SizedBox(height: 30),

            ElevatedButton.icon(
              icon: const Icon(Icons.picture_as_pdf),
              label: Text(AppLang.instance.t('download_report')),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => ResultScreen(result: result),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
