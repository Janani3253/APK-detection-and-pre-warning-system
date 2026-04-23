class ApkResult {
  // -------- App Info --------
  final String appName;
  final String packageName;
  final String versionName;
  final String appCategory;

  // -------- Risk --------
  final String verdict;
  final double riskScore;

  // -------- Permissions --------
  final List<String> expectedPermissions;
  final List<String> acceptablePermissions;
  final List<String> dangerousPermissions;

  // -------- Sandbox --------
  final bool sandboxInstalled;
  final bool sandboxLaunched;
  final bool sandboxCrashed;
  final double sandboxScore;

  ApkResult({
    required this.appName,
    required this.packageName,
    required this.versionName,
    required this.appCategory,
    required this.verdict,
    required this.riskScore,
    required this.expectedPermissions,
    required this.acceptablePermissions,
    required this.dangerousPermissions,
    required this.sandboxInstalled,
    required this.sandboxLaunched,
    required this.sandboxCrashed,
    required this.sandboxScore,
  });

  /// Convert backend JSON → Dart model
  factory ApkResult.fromJson(Map<String, dynamic> json) {
    final permissions = json['permission_analysis'] ?? {};
    final sandbox = permissions['sandbox'] ?? {};

    return ApkResult(
      appName: json['apk_details']?['app_name'] ?? '',
      packageName: json['apk_details']?['package_name'] ?? '',
      versionName: json['apk_details']?['version_name'] ?? '',
      appCategory: json['app_category'] ?? '',

      verdict: json['verdict'] ?? '',
      riskScore: (permissions['risk_score'] ?? 0).toDouble(),

      expectedPermissions:
      List<String>.from(permissions['expected'] ?? []),
      acceptablePermissions:
      List<String>.from(permissions['acceptable'] ?? []),
      dangerousPermissions:
      List<String>.from(permissions['dangerous'] ?? []),

      sandboxInstalled: sandbox['installed'] ?? false,
      sandboxLaunched: sandbox['launched'] ?? false,
      sandboxCrashed: sandbox['crashed'] ?? false,
      sandboxScore: (sandbox['sandbox_score'] ?? 0).toDouble(),
    );
  }
}