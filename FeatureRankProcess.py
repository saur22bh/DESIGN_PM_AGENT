from FeatureRanking import FeatureRankingProcess

from states import FeatureDesignGenerationState

def FeatureRankNode(state:FeatureDesignGenerationState):
    print("Enetered Feature Ranking Node")
    userInterest = state['UserInterest']
    FeatureGenerated = state['FeaturesGenerated']
    
    FeatureReview = state['FeatureReview']
    FeatureBucket = state['FeaturesBucketed']
    daat = 'Features : ' + "\n".join([f"- {f['feature_name']}: {f['description']}" for f in FeatureBucket['Highly Relevant']])
    FeatureRanks = FeatureRankingProcess.invoke({'user_interests':userInterest,'generated_features':daat})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated,'FeatureReview':FeatureReview,'FeaturesBucketed':FeatureBucket,"FeaturesRanked":FeatureRanks}