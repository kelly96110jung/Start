import 'package:flutter/material.dart';
import 'package:speech_to_text/speech_to_text.dart' as stt;

void main() {
  runApp(const MedexSTTDemo());
}

class MedexSTTDemo extends StatelessWidget {
  const MedexSTTDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: STTHomePage(),
    );
  }
}

class STTHomePage extends StatefulWidget {
  const STTHomePage({super.key});

  @override
  State<STTHomePage> createState() => _STTHomePageState();
}

class _STTHomePageState extends State<STTHomePage> {
  late stt.SpeechToText _speech;
  bool _isListening = false;
  String _recognizedText = "버튼을 누르고 의사 설명을 말해보세요.";

  @override
  void initState() {
    super.initState();
    _speech = stt.SpeechToText();
  }

  Future<void> _toggleListening() async {
    if (!_isListening) {
      bool available = await _speech.initialize(
        onStatus: (status) => debugPrint("STT STATUS: $status"),
        onError: (error) => debugPrint("STT ERROR: $error"),
      );

      if (available) {
        setState(() {
          _isListening = true;
          _recognizedText = "";
        });

        _speech.listen(
          localeId: 'ko_KR',
          listenMode: stt.ListenMode.dictation,
          partialResults: true,
          onResult: (result) {
            setState(() {
              _recognizedText = result.recognizedWords;
            });
          },
        );
      }
    } else {
      setState(() => _isListening = false);
      _speech.stop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("진료 설명 실시간 기록"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              "의사 설명 텍스트",
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            Expanded(
              child: Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  _recognizedText.isEmpty
                      ? "듣는 중..."
                      : _recognizedText,
                  style: const TextStyle(fontSize: 18),
                ),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton.icon(
              onPressed: _toggleListening,
              icon: Icon(_isListening ? Icons.stop : Icons.mic),
              label: Text(_isListening ? "녹음 종료" : "녹음 시작"),
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 14),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
