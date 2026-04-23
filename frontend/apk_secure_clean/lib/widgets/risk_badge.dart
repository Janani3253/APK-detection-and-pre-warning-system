import 'package:flutter/material.dart';

class RiskBadge extends StatelessWidget {
  final double risk;
  final String verdict;

  const RiskBadge({
    super.key,
    required this.risk,
    required this.verdict,
  });

  Color getColor() {
    if (risk < 20) return Colors.green;
    if (risk < 40) return Colors.lightGreen;
    if (risk < 60) return Colors.orange;
    if (risk < 80) return Colors.deepOrange;
    return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
    final color = getColor();

    return Card(
      elevation: 5,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            Text(
              "${risk.toStringAsFixed(1)}%",
              style: TextStyle(
                fontSize: 36,
                fontWeight: FontWeight.bold,
                color: color,
              ),
            ),
            const SizedBox(height: 6),
            Text(
              verdict,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w600,
                color: color,
              ),
            ),
          ],
        ),
      ),
    );
  }
}