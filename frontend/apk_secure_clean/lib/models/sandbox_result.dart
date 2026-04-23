/// Sandbox dynamic analysis result model
class SandboxResult {
  final bool installed;
  final bool launched;
  final bool crashed;
  final int sandboxScore;
  final List<String> observedBehaviors;
  final List<String> logs;

  const SandboxResult({
    required this.installed,
    required this.launched,
    required this.crashed,
    required this.sandboxScore,
    required this.observedBehaviors,
    required this.logs,
  });

  /// Create object from API JSON
  factory SandboxResult.fromJson(Map<String, dynamic>? json) {
    if (json == null) {
      return const SandboxResult(
        installed: false,
        launched: false,
        crashed: false,
        sandboxScore: 0,
        observedBehaviors: [],
        logs: [],
      );
    }

    return SandboxResult(
      installed: json['installed'] as bool? ?? false,
      launched: json['launched'] as bool? ?? false,
      crashed: json['crashed'] as bool? ?? false,
      sandboxScore: json['sandbox_score'] as int? ?? 0,
      observedBehaviors:
      List<String>.from(json['observed_behaviors'] ?? const []),
      logs: List<String>.from(json['logs'] ?? const []),
    );
  }

  /// Convert object back to JSON (optional but useful)
  Map<String, dynamic> toJson() {
    return {
      'installed': installed,
      'launched': launched,
      'crashed': crashed,
      'sandbox_score': sandboxScore,
      'observed_behaviors': observedBehaviors,
      'logs': logs,
    };
  }
}