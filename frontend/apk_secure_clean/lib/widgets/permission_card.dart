import 'package:flutter/material.dart';

class PermissionCard extends StatelessWidget {
  final String title;
  final List<String> permissions;
  final Color color;

  const PermissionCard({
    super.key,
    required this.title,
    required this.permissions,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 3,
      margin: const EdgeInsets.symmetric(vertical: 8),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: ExpansionTile(
        leading: Icon(Icons.lock, color: color),
        title: Text(
          title,
          style: TextStyle(
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
        children: permissions.isEmpty
            ? [
          const Padding(
            padding: EdgeInsets.all(12),
            child: Text(
              "No permissions detected 🎉",
              style: TextStyle(color: Colors.grey),
            ),
          )
        ]
            : permissions
            .map(
              (perm) => ListTile(
            dense: true,
            leading: Icon(Icons.circle, size: 8, color: color),
            title: Text(perm),
          ),
        )
            .toList(),
      ),
    );
  }
}