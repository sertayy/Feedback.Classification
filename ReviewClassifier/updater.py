import pickle
import json


if __name__ == '__main__':
    with open("classified_reviews.json", ) as f:
        with open("reviews.pickle", "rb") as p:
            reviews_pickle = pickle.load(p)
            reviews_json = json.load(f)
            #reviews_json["bug reports"].append(reviews_pickle[1][33])
            #reviews_json["feature requests"].append(reviews_pickle[1][21])
            #reviews_json["user experiences"].append(reviews_pickle[1][30])
            #reviews_json["ratings"].append(reviews_pickle[1][33])

    with open("classified_reviews.json", "w") as out:
        json.dump(reviews_json, out, ensure_ascii=False, indent=4)
