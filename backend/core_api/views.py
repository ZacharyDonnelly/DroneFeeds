"""Core API views"""
from typing import List
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test(request) -> List[str]:  # pylint: disable=unused-argument
    """Returns test string for now"""
    return Response("Testing this out!")
