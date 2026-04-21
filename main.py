from member1_data import load_data
from member2_feature_engineering import feature_engineering
from member3_analysis import analyze_data
from member4_model import train_model

# Step 1
train, test = load_data() 
# Step 2
train, test = feature_engineering(train, test)

# Step 3
analyze_data(train)

# Step 4
model = train_model(train)

print("Project completed successfully")