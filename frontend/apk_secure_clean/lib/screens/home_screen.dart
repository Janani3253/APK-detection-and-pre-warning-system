import 'dart:async';
import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:receive_sharing_intent/receive_sharing_intent.dart';

import '../services/api_service.dart';
import 'analysis_screen.dart';
import '../lang/lang.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _loading = false;
  StreamSubscription<List<SharedMediaFile>>? _intentSub;

  @override
  void initState() {
    super.initState();

    ReceiveSharingIntent.instance.getInitialMedia().then((files) {
      if (files.isNotEmpty) {
        _analyzeApk(File(files.first.path));
      }
    });

    _intentSub =
        ReceiveSharingIntent.instance.getMediaStream().listen((files) {
          if (files.isNotEmpty) {
            _analyzeApk(File(files.first.path));
          }
        });
  }

  @override
  void dispose() {
    _intentSub?.cancel();
    super.dispose();
  }

  Future<void> _pickApk() async {
    final result = await FilePicker.platform.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['apk'],
    );

    if (result != null && result.files.single.path != null) {
      _analyzeApk(File(result.files.single.path!));
    }
  }

  Future<void> _analyzeApk(File apk) async {
    setState(() => _loading = true);

    try {
      final response = await ApiService.uploadApk(apk);

      if (!mounted) return;

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (_) => AnalysisScreen(result: response),
        ),
      );
    } catch (e) {
      if (!mounted) return;

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("${AppLang.instance.t('error')}: $e"),
        ),
      );
    }

    setState(() => _loading = false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade100,
      appBar: AppBar(
        title: Text(AppLang.instance.t('app_title')),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.language),
            onPressed: () {
              AppLang.instance.switchLang(
                AppLang.instance.current == 'en' ? 'ta' : 'en',
              );
            },
          ),
        ],
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.security, size: 90, color: Colors.blue),

              const SizedBox(height: 25),

              Text(
                AppLang.instance.t('home_hint'),
                style: const TextStyle(
                    fontSize: 20, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),

              const SizedBox(height: 40),

              ElevatedButton.icon(
                icon: const Icon(Icons.upload_file),
                label: Text(AppLang.instance.t('select_apk')),
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(
                      horizontal: 30, vertical: 15),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
                onPressed: _loading ? null : _pickApk,
              ),

              const SizedBox(height: 30),

              if (_loading)
                Column(
                  children: [
                    const CircularProgressIndicator(),
                    const SizedBox(height: 12),
                    Text(AppLang.instance.t('analyzing')),
                  ],
                ),
            ],
          ),
        ),
      ),
    );
  }
}
