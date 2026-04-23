import 'package:flutter/material.dart';

class SandboxCard extends StatelessWidget {
  final Map<String, dynamic> sandbox;

  const SandboxCard({
    super.key,
    required this.sandbox,
  });

  @override
  Widget build(BuildContext context) {
    final logs = List<String>.from(sandbox['logs'] ?? []);

    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "Sandbox Analysis 🧪",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 10),

            _row("Installed", sandbox['installed']),
            _row("Launched", sandbox['launched']),
            _row("Crashed", sandbox['crashed']),
            _row(
              "Sandbox Risk",
              "${sandbox['sandbox_score']}%",
            ),

            const Divider(height: 25),

            const Text(
              "Sandbox Logs",
              style: TextStyle(fontWeight: FontWeight.w600),
            ),

            const SizedBox(height: 8),

            ...logs.map(
                  (log) => Text(
                "• $log",
                style: const TextStyle(fontSize: 13),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _row(String label, dynamic value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Expanded(child: Text(label)),
          Text(
            value.toString(),
            style: const TextStyle(fontWeight: FontWeight.bold),
          ),
        ],
      ),
    );
  }
}
