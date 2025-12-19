package demo

import nlp.PostProcessor

fun main() {
    val sttLikeInput =
        "크레아티닌 1.29 나오셨고요 단백질 섭취 조금 조절해주세요 " +
                "수분 섭취 꾸준히 하시고 3개월 뒤에 재검 오시면 됩니다 " +
                "전화질은 괜찮고 칼륭 수치는 정상이에요"

    val result = PostProcessor.process(sttLikeInput)

    println("===== [원문 STT 텍스트] =====")
    println(sttLikeInput)

    println("\n===== [교정 후 텍스트] =====")
    println(result.corrected)

    println("\n===== [문장 분리 결과] =====")
    result.sentences.forEachIndexed { i, s ->
        println("${i + 1}. $s")
    }

    println("\n===== [요약 결과] =====")
    result.summary.forEach {
        println("- $it")
    }

    println("\n===== [JSON 구조화 결과] =====")
    println(result.jsonPretty)
}
