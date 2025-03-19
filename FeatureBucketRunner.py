from FeatureBuckets import FeatureBucketrocess 

from states import FeatureDesignGenerationState

def FeatureBucketNode(state:FeatureDesignGenerationState):
    print("Enetered Feature Bucketing Node")
    userInterest = state['UserInterest']
    FeatureGenerated = state['FeaturesGenerated']
    
    FeatureReview = state['FeatureReview']
    data_to_be_sent = 'Features along with their descriptions : ' + '\n' + "\n".join([f"- {f['feature_name']}: {f['description']}" for f in FeatureReview['continued_features']])
    FeatureBucket = FeatureBucketrocess.invoke({'features':data_to_be_sent,'user_interests':userInterest})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated,'FeatureReview':FeatureReview,'FeaturesBucketed':FeatureBucket}