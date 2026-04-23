import 'package:flutter/material.dart';
import 'screens/home_screen.dart';
import 'lang/lang.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const ApkSecureApp());
}

class ApkSecureApp extends StatelessWidget {
  const ApkSecureApp({super.key});

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: AppLang.instance,
      builder: (context, _) {
        return MaterialApp(
          title: 'APK Secure',
          debugShowCheckedModeBanner: false,

          theme: ThemeData(
            useMaterial3: true,
            colorSchemeSeed: Colors.indigo,
            scaffoldBackgroundColor: const Color(0xFFF4F6FA),

            cardTheme: const CardThemeData(
              elevation: 6,
              margin: EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.all(Radius.circular(18)),
              ),
            ),

            appBarTheme: const AppBarTheme(
              centerTitle: true,
              backgroundColor: Colors.transparent,
              elevation: 0,
              titleTextStyle: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Colors.black,
              ),
            ),

            elevatedButtonTheme: ElevatedButtonThemeData(
              style: ElevatedButton.styleFrom(
                minimumSize: const Size(double.infinity, 54),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
                textStyle: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),

            textTheme: const TextTheme(
              headlineMedium: TextStyle(fontWeight: FontWeight.bold),
              bodyMedium: TextStyle(fontSize: 15),
            ),
          ),

          home: const HomeScreen(),
        );
      },
    );
  }
}
