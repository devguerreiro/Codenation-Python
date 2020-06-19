from rest_framework.decorators import api_view
from rest_framework.response import Response

from collections import Counter


@api_view(["POST"])
def lambda_function(request):
    question_data = request.data.get("question")

    solution_data = [
        item
        for items, count in Counter(question_data).most_common()
        for item in [items] * count
    ]

    return Response(data={"solution": solution_data})
