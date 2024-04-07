from django.http import JsonResponse
from django.views import View

class MoviesListApi(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        # Получение и обработка данных
        print('fffff')
        return JsonResponse(
            {
                "count": 1000,
                "total_pages": 20,
                "prev": 1,
                "next": 2,
                "results": [
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "title": "Crescent Star",
                        "description": "In 1944, the Germans began rounding up the Jews of Rhodes.",
                        "creation_date": "2024-04-07",
                        "rating": 7.9,
                        "type": "movie",
                        "genres": [
                            "Drama",
                            "Short"
                        ],
                        "actors": [
                            "Darrell Geer",
                            "Michael Bond"
                        ],
                        "directors": [
                            "Turgut Turk Adiguzel"
                        ],
                        "writers": [
                            "Turgut Turk Adiguzel"
                        ]
                    }
                ]
            }
        )