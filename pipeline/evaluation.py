def evaluate_system(run_query_fn):
    test_cases = [
        {
            "question": "How many PTO days do employees get?",
            "expected": "20 days"
        },
        {
            "question": "What is the parental leave duration?",
            "expected": "12 weeks"
        }
    ]

    results = []

    for test in test_cases:
        output = run_query_fn(test["question"])

        top_result = output[0]["text"].lower()
        expected = test["expected"].lower()

        correct = expected in top_result

        results.append({
            "question": test["question"],
            "expected": test["expected"],
            "retrieved_text": top_result,
            "correct": correct
        })

    accuracy = sum(r["correct"] for r in results) / len(results)

    return results, accuracy