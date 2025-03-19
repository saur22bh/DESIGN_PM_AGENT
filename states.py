from typing import Dict, Any, List, Optional, TypedDict

class FeatureDesignGenerationState(TypedDict):
    """
    Representing state of our graph

    Attributes : 
    1 - UserInterest : Interest input given by user
    2 - FeaturesGenerated : Features Generated by LLM
    3 - FeatureReviewe : Features Continued
    4 - FeaturesBucketed : Features bucketed basis the value they offer
    5 - FeaturesRanked : Features ranked basis various factors
    6 - WebsiteDescriptions : Web UI description for top ranked feature
    7 - CombinedFeatureDescription : Combined feature generated from a list of generated features
    8 - Code : Code generated by combined feature
    """

    UserInterest : str 
    FeaturesGenerated : Optional[List[str]] = None
    FeatureReview : Optional[List[str]] = None
    FeaturesBucketed : Optional[List[str]] = None
    FeaturesRanked : Optional[List[str]] = None
    WebsiteDescriptions : Optional[List[str]] = None
    CombinedFeatureDescription : Optional[List[str]] = None
    Code : Optional[List[str]] = None