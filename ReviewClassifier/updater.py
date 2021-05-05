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
    bug_1 = [
        reviews_pickle[1][8],
        reviews_pickle[1][14],
        reviews_pickle[1][17],
        reviews_pickle[1][19],
        reviews_pickle[1][24],
        reviews_pickle[1][28],
        reviews_pickle[1][31],
        reviews_pickle[1][33],
        reviews_pickle[1][34],
        reviews_pickle[1][35],
        reviews_pickle[1][37],
        reviews_pickle[1][43],
        reviews_pickle[1][46],
        reviews_pickle[1][47],
        reviews_pickle[1][51],
        reviews_pickle[1][52],
        reviews_pickle[1][55],
        reviews_pickle[1][68],
        reviews_pickle[1][69],
        reviews_pickle[1][194],
        reviews_pickle[1][197],
        reviews_pickle[1][198],
        reviews_pickle[1][206],
        reviews_pickle[1][211],
        reviews_pickle[1][218],
        reviews_pickle[1][222],
        reviews_pickle[1][225],
        reviews_pickle[1][229],
        reviews_pickle[1][232],
        reviews_pickle[1][233],
        reviews_pickle[1][235],
        reviews_pickle[1][246],
        reviews_pickle[1][247],
        reviews_pickle[1][248],
        reviews_pickle[1][251],
        reviews_pickle[1][259],
        reviews_pickle[1][261],
        reviews_pickle[1][264],
        reviews_pickle[1][282],
        reviews_pickle[1][283]
    ]
    bug_2 = [
        reviews_pickle[2][2],
        reviews_pickle[2][3],
        reviews_pickle[2][5],
        reviews_pickle[2][22],
        reviews_pickle[2][24],
        reviews_pickle[2][28],
        reviews_pickle[2][36],
        reviews_pickle[2][37],
        reviews_pickle[2][40],
        reviews_pickle[2][42],
        reviews_pickle[2][44],
        reviews_pickle[2][45],
        reviews_pickle[2][46]
    ]
    bug_3 = [
        reviews_pickle[3][3],
        reviews_pickle[3][32],
        reviews_pickle[3][18],
        reviews_pickle[3][63],
        reviews_pickle[3][70],
        reviews_pickle[3][74]
    ]
    bug_4 = [
        reviews_pickle[4][149],
        reviews_pickle[4][164],
        reviews_pickle[4][175]
    ]

    feature_1 = [
        reviews_pickle[1][12],
        reviews_pickle[1][18],
        reviews_pickle[1][21],
        reviews_pickle[1][38],
        reviews_pickle[1][40],
        reviews_pickle[1][199],
        reviews_pickle[1][204],
        reviews_pickle[1][208],
        reviews_pickle[1][227],
        reviews_pickle[1][231],
        reviews_pickle[1][244],
        reviews_pickle[1][253],
        reviews_pickle[1][265],
        reviews_pickle[1][266],
        reviews_pickle[1][272],
        reviews_pickle[1][277],
        reviews_pickle[1][292]
    ]
    feature_2 = [
        reviews_pickle[2][0],
        reviews_pickle[2][1],
        reviews_pickle[2][6],
        reviews_pickle[2][12],
        reviews_pickle[2][20],
        reviews_pickle[2][32],
        reviews_pickle[2][47]
    ]
    feature_3 = [
        reviews_pickle[3][0],
        reviews_pickle[3][5],
        reviews_pickle[3][6],
        reviews_pickle[3][8],
        reviews_pickle[3][9],
        reviews_pickle[3][11],
        reviews_pickle[3][13],
        reviews_pickle[3][20],
        reviews_pickle[3][25],
        reviews_pickle[3][26],
        reviews_pickle[3][30],
        reviews_pickle[3][31],
        reviews_pickle[3][37],
        reviews_pickle[3][58],
        reviews_pickle[3][66]
    ]
    feature_4 = [
        reviews_pickle[4][159],
        reviews_pickle[4][184],
        reviews_pickle[4][193],
        reviews_pickle[4][202],
        reviews_pickle[4][162],
        reviews_pickle[4][167],
        reviews_pickle[4][173]
    ]
    feature_5 = [
        reviews_pickle[5][1070],
        reviews_pickle[5][1079]
    ]

    user_ex_1 = [
        reviews_pickle[1][0],
        reviews_pickle[1][1],
        reviews_pickle[1][4],
        reviews_pickle[1][5],
        reviews_pickle[1][10],
        reviews_pickle[1][17],
        reviews_pickle[1][22],
        reviews_pickle[1][29],
        reviews_pickle[1][30],
        reviews_pickle[1][44],
        reviews_pickle[1][49],
        reviews_pickle[1][54],
        reviews_pickle[1][57],
        reviews_pickle[1][60],
        reviews_pickle[1][62],
        reviews_pickle[1][67],
        reviews_pickle[1][75],
        reviews_pickle[1][78],
        reviews_pickle[1][79],
        reviews_pickle[1][192],
        reviews_pickle[1][195],
        reviews_pickle[1][196],
        reviews_pickle[1][200],
        reviews_pickle[1][205],
        reviews_pickle[1][207],
        reviews_pickle[1][214],
        reviews_pickle[1][215],
        reviews_pickle[1][216],
        reviews_pickle[1][230],
        reviews_pickle[1][239],
        reviews_pickle[1][242],
        reviews_pickle[1][243],
        reviews_pickle[1][244],
        reviews_pickle[1][252],
        reviews_pickle[1][255],
        reviews_pickle[1][258],
        reviews_pickle[1][267],
        reviews_pickle[1][268],
        reviews_pickle[1][269],
        reviews_pickle[1][281],
        reviews_pickle[1][293],
        reviews_pickle[1][294]
    ]
    user_ex_2 = [
        reviews_pickle[2][3],
        reviews_pickle[2][4],
        reviews_pickle[2][7],
        reviews_pickle[2][9],
        reviews_pickle[2][10],
        reviews_pickle[2][13],
        reviews_pickle[2][16],
        reviews_pickle[2][19],
        reviews_pickle[2][21],
        reviews_pickle[2][23],
        reviews_pickle[2][38],
        reviews_pickle[2][39],
        reviews_pickle[2][43]
    ]
    user_ex_3 = [
        reviews_pickle[3][4],
        reviews_pickle[3][7],
        reviews_pickle[3][14],
        reviews_pickle[3][19],
        reviews_pickle[3][21],
        reviews_pickle[3][29],
        reviews_pickle[3][34],
        reviews_pickle[3][35],
        reviews_pickle[3][38],
        reviews_pickle[3][60],
        reviews_pickle[3][61],
        reviews_pickle[3][64],
        reviews_pickle[3][65],
        reviews_pickle[3][73],
        reviews_pickle[3][74]
    ]
    user_ex_4 = [
        reviews_pickle[4][126],
        reviews_pickle[4][128],
        reviews_pickle[4][130],
        reviews_pickle[4][131],
        reviews_pickle[4][137],
        reviews_pickle[4][146],
        reviews_pickle[4][153],
        reviews_pickle[4][185],
        reviews_pickle[4][188],
        reviews_pickle[4][191],
        reviews_pickle[4][199],
        reviews_pickle[4][200],
        reviews_pickle[4][204],
        reviews_pickle[4][170],
        reviews_pickle[4][171],
        reviews_pickle[4][176],
        reviews_pickle[4][178]
    ]
    user_ex_5 = [
        reviews_pickle[5][1004],
        reviews_pickle[5][1007],
        reviews_pickle[5][1011],
        reviews_pickle[5][1021],
        reviews_pickle[5][1022],
        reviews_pickle[5][1025],
        reviews_pickle[5][1031],
        reviews_pickle[5][1034],
        reviews_pickle[5][1050],
        reviews_pickle[5][1055],
        reviews_pickle[5][1085],
        reviews_pickle[5][1092]
    ]

    ratings_1 = [
        reviews_pickle[1][23],
        reviews_pickle[1][25],
        reviews_pickle[1][26],
        reviews_pickle[1][30],
        reviews_pickle[1][27],
        reviews_pickle[1][33],
        reviews_pickle[1][39],
        reviews_pickle[1][48],
        reviews_pickle[1][51],
        reviews_pickle[1][54],
        reviews_pickle[1][58],
        reviews_pickle[1][61],
        reviews_pickle[1][62],
        reviews_pickle[1][64],
        reviews_pickle[1][67],
        reviews_pickle[1][75],
        reviews_pickle[1][208],
        reviews_pickle[1][209],
        reviews_pickle[1][214],
        reviews_pickle[1][224],
        reviews_pickle[1][25],
        reviews_pickle[1][402],
        reviews_pickle[1][249],
        reviews_pickle[1][254],
        reviews_pickle[1][257],
        reviews_pickle[1][258],
        reviews_pickle[1][261],
        reviews_pickle[1][262],
        reviews_pickle[1][266],
        reviews_pickle[1][270],
        reviews_pickle[1][61],
        reviews_pickle[1][25],
        reviews_pickle[1][298]
    ]
    ratings_2 = [
        reviews_pickle[2][15],
        reviews_pickle[2][25],
        reviews_pickle[2][35],
        reviews_pickle[2][41]
    ]
    ratings_3 = [
        reviews_pickle[3][2],
        reviews_pickle[3][8],
        reviews_pickle[3][10],
        reviews_pickle[3][15],
        reviews_pickle[3][17],
        reviews_pickle[3][21],
        reviews_pickle[3][22],
        reviews_pickle[3][24],
        reviews_pickle[3][27],
        reviews_pickle[3][28],
        reviews_pickle[3][33],
        reviews_pickle[3][36],
        reviews_pickle[3][39],
        reviews_pickle[3][40],
        reviews_pickle[3][60],
        reviews_pickle[3][62],
        reviews_pickle[3][67],
        reviews_pickle[3][68],
        reviews_pickle[3][69],
        reviews_pickle[3][71],
        reviews_pickle[3][72],
        reviews_pickle[3][28],
        reviews_pickle[3][28],
        reviews_pickle[3][28],
        reviews_pickle[3][28],
        reviews_pickle[3][28],
        reviews_pickle[3][28]
    ]
    ratings_4 = [
        reviews_pickle[4][121],
        reviews_pickle[4][123],
        reviews_pickle[4][124],
        reviews_pickle[4][125],
        reviews_pickle[4][126],
        reviews_pickle[4][129],
        reviews_pickle[4][46],
        reviews_pickle[4][139],
        reviews_pickle[4][142],
        reviews_pickle[4][144],
        reviews_pickle[4][153],
        reviews_pickle[4][155],
        reviews_pickle[4][156],
        reviews_pickle[4][180],
        reviews_pickle[4][183],
        reviews_pickle[4][185],
        reviews_pickle[4][186],
        reviews_pickle[4][187],
        reviews_pickle[4][190],
        reviews_pickle[4][193],
        reviews_pickle[4][195],
        reviews_pickle[4][108],
        reviews_pickle[4][129],
        reviews_pickle[4][201],
        reviews_pickle[4][204],
        reviews_pickle[4][162],
        reviews_pickle[4][163],
        reviews_pickle[4][165],
        reviews_pickle[4][166],
        reviews_pickle[4][167],
        reviews_pickle[4][169],
        reviews_pickle[4][4],
        reviews_pickle[4][174],
        reviews_pickle[4][177],
        reviews_pickle[4][178],
        reviews_pickle[4][46]
    ]
    ratings_5 = [
        reviews_pickle[5][1000],
        reviews_pickle[5][1005],
        reviews_pickle[5][577],
        reviews_pickle[5][1014],
        reviews_pickle[5][1017],
        reviews_pickle[5][1024],
        reviews_pickle[5][1025],
        reviews_pickle[5][1029],
        reviews_pickle[5][1032],
        reviews_pickle[5][1038],
        reviews_pickle[5][1040],
        reviews_pickle[5][1049],
        reviews_pickle[5][1055],
        reviews_pickle[5][1056],
        reviews_pickle[5][1058],
        reviews_pickle[5][1064],
        reviews_pickle[5][1066],
        reviews_pickle[5][1076],
        reviews_pickle[5][1077],
        reviews_pickle[5][1084],
        reviews_pickle[5][1085],
        reviews_pickle[5][1086],
        reviews_pickle[5][1091],
        reviews_pickle[5][1094],
        reviews_pickle[5][273]
    ]

    json_helper(bug_1, 1, "bug report")
    json_helper(bug_2, 2, "bug report")
    json_helper(bug_3, 3, "bug report")
    json_helper(bug_4, 4, "bug report")
    json_helper(feature_1, 1, "feature request")
    json_helper(feature_2, 2, "feature request")
    json_helper(feature_3, 3, "feature request")
    json_helper(feature_4, 4, "feature request")
    json_helper(feature_5, 5, "feature request")
    json_helper(user_ex_1, 1, "user experience")
    json_helper(user_ex_2, 2, "user experience")
    json_helper(user_ex_3, 3, "user experience")
    json_helper(user_ex_4, 4, "user experience")
    json_helper(user_ex_5, 5, "user experience")
    json_helper(ratings_1, 1, "ratings")
    json_helper(ratings_2, 2, "ratings")
    json_helper(ratings_3, 3, "ratings")
    json_helper(ratings_4, 4, "ratings")
    json_helper(ratings_5, 5, "ratings")

    with open("classified_reviews.json", "w") as out:
        json.dump(reviews_json, out, ensure_ascii=False, indent=4)
