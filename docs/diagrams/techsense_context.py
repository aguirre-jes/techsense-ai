from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.engagement import SimpleEmailServiceSes
from diagrams.aws.general import InternetAlt1, Users
from diagrams.aws.integration import Eventbridge
from diagrams.aws.ml import Bedrock


with Diagram("TechSense MVP Context", show=False, direction="LR", outformat="png"):
    reader = Users("TechSense Reader")
    schedule = Eventbridge("Friday Schedule")

    with Cluster("RSS Sources"):
        ietf = InternetAlt1("IETF Datatracker")
        aws_blog = InternetAlt1("AWS Open Source Blog")
        cloudflare = InternetAlt1("Cloudflare Engineering")

    app = Lambda("TechSense MVP")
    store = Dynamodb("Article Store")
    model = Bedrock("Claude Haiku")
    email = SimpleEmailServiceSes("Weekly Email")

    [ietf, aws_blog, cloudflare] >> app
    schedule >> app
    app >> store
    app >> model
    app >> email >> reader
