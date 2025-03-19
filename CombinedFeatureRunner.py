


from Combinedfeature import CombinedFeatureProcess

from states import FeatureDesignGenerationState

def CombinedFeatureNode(state:FeatureDesignGenerationState):
    print("Enetered Combined Feature Ranking Node")
    userInterest = state['UserInterest']
    FeatureGenerated = state['FeaturesGenerated']
    FeatureReview = state['FeatureReview']
    FeatureBucket = state['FeaturesBucketed']
    FeatureRanks = state['FeaturesRanked']
    # FeaturesGenerated = 'Features : ' + "\n".join([f"- {f['feature_name']}: {f['description']}" for f in FeatureBucket['Highly Relevant']]) + "\n".join([f"- {f['feature_name']}: {f['description']}" for f in FeatureBucket['Somewhat relevant']])
    WebDescriptions = state['WebsiteDescriptions']
    CombinedFeatures = CombinedFeatureProcess.invoke({'list_of_features':FeatureGenerated})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated,'FeatureReview':FeatureReview,'FeaturesBucketed':FeatureBucket,"FeaturesRanked":FeatureRanks,"WebsiteDescriptions":WebDescriptions,"CombinedFeatureDescription":CombinedFeatures}