class MongoFilter:

    @staticmethod
    def filter_books(collections, filters):
        mongo_query = {}

        selected_rows = {'_id': 0}

        order_mapping = {"desc": -1,
                         "asc": 1}

        numeric_mapping = {
            "average_rating": float,
            "original_publication_year": int,
            "price": int
        }

        for key, value in filters.items():
            if key != "order" and key not in numeric_mapping:
                mongo_query[key] = {'$regex': value, '$options': 'i'}

        for key in numeric_mapping:
            if key in filters:
                function = numeric_mapping[key]
                mongo_query[key] = function(filters[key])

        if "order" in filters:
            order = order_mapping[filters["order"]]
            results = collections.find(mongo_query, selected_rows).sort("price", order)
        else:
            results = collections.find(mongo_query, selected_rows)

        return {'results': [doc for doc in results]}

