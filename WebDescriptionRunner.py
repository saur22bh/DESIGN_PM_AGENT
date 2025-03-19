from WebDescription import WebDescProcess 

from states import FeatureDesignGenerationState

def WebDescNode(state:FeatureDesignGenerationState):
    print("Enetered Website Description for top rank node")
    userInterest = state['UserInterest']
    FeatureGenerated = state['FeaturesGenerated']
    
    FeatureReview = state['FeatureReview']
    FeatureBucket = state['FeaturesBucketed']
    FeatureRanks = state['FeaturesRanked']
    rank_1_entry = None
    for key, value in FeatureRanks.items():
        if value['rank'] == 1:
            rank_1_entry = {key: value}
            break

    feature_name = list(rank_1_entry.keys())[0]
    desc = rank_1_entry[feature_name]['description']
    WebDescriptions = WebDescProcess.invoke({'FeatureName':feature_name,"feature":desc})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated,'FeatureReview':FeatureReview,'FeaturesBucketed':FeatureBucket,"FeaturesRanked":FeatureRanks,"WebsiteDescriptions":WebDescriptions}