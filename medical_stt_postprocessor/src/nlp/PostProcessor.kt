package nlp

import kotlin.math.min

object PostProcessor {

    data class Exam(
        val name: String,
        val value: Double,
        val unit: String,
        val meaning: String? = null
    )

    data class Result(
        val corrected: String,
        val sentences: List<String>,
        val summary: List<String>,
        val jsonPretty: String
    )

    // 의료 용어 사전 (데모용)
    private val medicalTerms = listOf(
        "전해질", "크레아티닌", "칼륨", "나트륨", "단백뇨"
    )

    // STT 흔한 오인식 교정
    private val correctionMap = mapOf(
        "전화질" to "전해질",
        "칼륭" to "칼륨",
        "단백류" to "단백뇨"
    )

    private val valueRegex =
        Regex("""([0-9]+(?:\.[0-9]+)?)\s?(mg/dL|mmol/L)""")

    fun process(rawText: String): Result {
        val corrected = correctText(rawText)
        val sentences = splitSentences(corrected)
        val summary = summarize(sentences)
        val json = buildJson(sentences)

        return Result(
            corrected = corrected,
            sentences = sentences,
            summary = summary,
            jsonPretty = json
        )
    }

    // -----------------------
    // 1. 텍스트 교정
    // -----------------------
    private fun correctText(text: String): String {
        var result = text
        correctionMap.forEach { (wrong, right) ->
            result = result.replace(wrong, right)
        }
        return result
    }

    // -----------------------
    // 2. 문장 분리
    // -----------------------
    private fun splitSentences(text: String): List<String> {
        return text
            .replace("하시면 됩니다", "하시면 됩니다|")
            .replace("오시면 됩니다", "오시면 됩니다|")
            .replace("이구요", "이구요|")
            .split("|")
            .map { it.trim() }
            .filter { it.isNotEmpty() }
    }

    // -----------------------
    // 3. 요약 생성
    // -----------------------
    private fun summarize(sentences: List<String>): List<String> {
        return sentences.take(3)
    }

    // -----------------------
    // 4. JSON 구조화
    // -----------------------
    private fun buildJson(sentences: List<String>): String {
        val content = sentences.joinToString(",\n") {
            "  \"${it}\""
        }

        return """
{
  "doctor_summary": [
$content
  ]
}
        """.trimIndent()
    }

    private fun levenshtein(a: String, b: String): Int {
        val dp = Array(a.length + 1) { IntArray(b.length + 1) }
        for (i in 0..a.length) dp[i][0] = i
        for (j in 0..b.length) dp[0][j] = j

        for (i in 1..a.length) {
            for (j in 1..b.length) {
                val cost = if (a[i - 1] == b[j - 1]) 0 else 1
                dp[i][j] = min(
                    min(dp[i - 1][j] + 1, dp[i][j - 1] + 1),
                    dp[i - 1][j - 1] + cost
                )
            }
        }
        return dp[a.length][b.length]
    }
}
