import pickle
import json

reviews_json = []


def json_helper(review_list, rating, cat_type):
    for elem in review_list:
        reviews_json.append({
            "review": elem[1:],
            "rating": rating,
            "category": cat_type
        })


if __name__ == '__main__':
    with open("reviews.pickle", "rb") as p:
        reviews_pickle = pickle.load(p)
    bug_1 = [reviews_pickle[1][301], reviews_pickle[1][305], reviews_pickle[1][312], reviews_pickle[1][313],
             reviews_pickle[1][315], reviews_pickle[1][320], reviews_pickle[1][324], reviews_pickle[1][326],
             reviews_pickle[1][334], reviews_pickle[1][335], reviews_pickle[1][338], reviews_pickle[1][339],
             reviews_pickle[1][342], reviews_pickle[1][341], reviews_pickle[1][343], reviews_pickle[1][345],
             reviews_pickle[1][347], reviews_pickle[1][363], reviews_pickle[1][367], reviews_pickle[1][372],
             reviews_pickle[1][376], reviews_pickle[1][383], reviews_pickle[1][390], reviews_pickle[1][391],
             reviews_pickle[1][393], reviews_pickle[1][401]]
    bug_3 = [reviews_pickle[3][91]]
    bug_4 = [reviews_pickle[4][216], reviews_pickle[4][221], reviews_pickle[4][227], reviews_pickle[4][240],
             reviews_pickle[4][241], reviews_pickle[4][245]]

    feature_1 = [reviews_pickle[1][303], reviews_pickle[1][304], reviews_pickle[1][308], reviews_pickle[1][323],
                 reviews_pickle[1][364], reviews_pickle[1][365], reviews_pickle[1][377], reviews_pickle[1][380],
                 reviews_pickle[1][381], reviews_pickle[1][385], reviews_pickle[1][396]]
    feature_3 = [reviews_pickle[3][78], reviews_pickle[3][79], reviews_pickle[3][90]]
    feature_4 = [reviews_pickle[4][211], reviews_pickle[4][214],
                 reviews_pickle[4][217], reviews_pickle[4][219], reviews_pickle[4][224], reviews_pickle[4][225],
                 reviews_pickle[4][229], reviews_pickle[4][230], reviews_pickle[4][232], reviews_pickle[4][233],
                 reviews_pickle[4][237], reviews_pickle[4][238], reviews_pickle[4][242], reviews_pickle[4][247],
                 reviews_pickle[4][252], reviews_pickle[4][267], reviews_pickle[4][268], reviews_pickle[4][272],
                 reviews_pickle[4][279]]

    user_ex_1 = [reviews_pickle[1][301], reviews_pickle[1][302], reviews_pickle[1][306], reviews_pickle[1][307],
                 reviews_pickle[1][309], reviews_pickle[1][311], reviews_pickle[1][314], reviews_pickle[1][316],
                 reviews_pickle[1][318], reviews_pickle[1][319], reviews_pickle[1][322], reviews_pickle[1][327],
                 reviews_pickle[1][329], reviews_pickle[1][340], reviews_pickle[1][344], reviews_pickle[1][346],
                 reviews_pickle[1][348], reviews_pickle[1][350], reviews_pickle[1][351], reviews_pickle[1][352],
                 reviews_pickle[1][354], reviews_pickle[1][357], reviews_pickle[1][361], reviews_pickle[1][362],
                 reviews_pickle[1][366], reviews_pickle[1][349], reviews_pickle[1][369], reviews_pickle[1][370],
                 reviews_pickle[1][373], reviews_pickle[1][375], reviews_pickle[1][378], reviews_pickle[1][382],
                 reviews_pickle[1][388], reviews_pickle[1][392], reviews_pickle[1][393], reviews_pickle[1][399],
                 reviews_pickle[1][400]]
    user_ex_3 = [reviews_pickle[3][81], reviews_pickle[3][83], reviews_pickle[3][85], reviews_pickle[3][86],
                 reviews_pickle[3][89]]
    user_ex_4 = [reviews_pickle[4][209], reviews_pickle[4][218], reviews_pickle[4][233], reviews_pickle[4][249],
                 reviews_pickle[4][251], reviews_pickle[4][253], reviews_pickle[4][255], reviews_pickle[4][257],
                 reviews_pickle[4][258], reviews_pickle[4][261], reviews_pickle[4][270], reviews_pickle[4][276],
                 ]

    ratings_1 = [reviews_pickle[1][300], reviews_pickle[1][310], reviews_pickle[1][321], reviews_pickle[1][325],
                 reviews_pickle[1][333], reviews_pickle[1][336], reviews_pickle[1][337], reviews_pickle[1][343],
                 reviews_pickle[1][333], reviews_pickle[1][349], reviews_pickle[1][353], reviews_pickle[1][355],
                 reviews_pickle[1][356], reviews_pickle[1][359], reviews_pickle[1][368], reviews_pickle[1][374],
                 reviews_pickle[1][384], reviews_pickle[1][387], reviews_pickle[1][389], reviews_pickle[1][394],
                 reviews_pickle[1][396], reviews_pickle[1][402]]
    ratings_3 = [reviews_pickle[3][76], reviews_pickle[3][77], reviews_pickle[3][80], reviews_pickle[3][87],
                 reviews_pickle[3][88]]
    ratings_4 = [reviews_pickle[4][205], reviews_pickle[4][206], reviews_pickle[4][207], reviews_pickle[4][208],
                 reviews_pickle[4][210], reviews_pickle[4][212], reviews_pickle[4][213], reviews_pickle[4][215],
                 reviews_pickle[4][218], reviews_pickle[4][220], reviews_pickle[4][223], reviews_pickle[4][224],
                 reviews_pickle[4][228], reviews_pickle[4][226], reviews_pickle[4][231], reviews_pickle[4][234],
                 reviews_pickle[4][235], reviews_pickle[4][239], reviews_pickle[4][243], reviews_pickle[4][244],
                 reviews_pickle[4][246], reviews_pickle[4][248], reviews_pickle[4][250], reviews_pickle[4][251],
                 reviews_pickle[4][252], reviews_pickle[4][254], reviews_pickle[4][256], reviews_pickle[4][259],
                 reviews_pickle[4][260], reviews_pickle[4][262], reviews_pickle[4][263], reviews_pickle[4][264],
                 reviews_pickle[4][265], reviews_pickle[4][266], reviews_pickle[4][269], reviews_pickle[4][270],
                 reviews_pickle[4][271], reviews_pickle[4][273], reviews_pickle[4][274], reviews_pickle[4][275],
                 reviews_pickle[4][278], reviews_pickle[4][280], reviews_pickle[4][281]]

    json_helper(bug_1, 1, "bug report")
    json_helper(bug_3, 3, "bug report")
    json_helper(bug_4, 4, "bug report")
    json_helper(feature_1, 1, "feature request")
    json_helper(feature_3, 3, "feature request")
    json_helper(feature_4, 4, "feature request")
    json_helper(user_ex_1, 1, "user experience")
    json_helper(user_ex_3, 3, "user experience")
    json_helper(user_ex_4, 4, "user experience")
    json_helper(ratings_1, 1, "ratings")
    json_helper(ratings_3, 3, "ratings")
    json_helper(ratings_4, 4, "ratings")

    with open("classified_reviews.json", "w") as out:
        json.dump(reviews_json, out, ensure_ascii=False, indent=4)
