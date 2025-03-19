from FeatureReviews import FeatureReviewProcess


from states import FeatureDesignGenerationState

def FeatureReviewerNode(state:FeatureDesignGenerationState):
    print("Enetered Feature Reviewer Node")
    userInterest = state['UserInterest']
    FeatureGenerated = state['FeaturesGenerated']
    FeatureReviewed = FeatureReviewProcess.invoke({'user_interests':userInterest,'generated_features':FeatureGenerated})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated,"FeatureReview":FeatureReviewed}