import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score,roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

def train_model():
    # load dataset
    df = pd.read_csv("features.csv")

    # Split features and target
    X = df.drop(columns=['readmitted','admission_id'])
    y = df['readmitted']

    # test split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    #regression training
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train,y_train)

    # predict and evaluate
    y_pred =model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1]

    print("\n Classification_report:")
    print(classification_report(y_test,y_pred))

    print("\n Confusion Matrix:")
    cm = confusion_matrix(y_test,y_pred)
    sns.heatmap(cm,annot=True,fmt='d',cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    roc_score = roc_auc_score(y_test,y_proba)
    print(f"\n ROC AUC Score: {roc_score:.2f}")

    # plot ROC Curve
    fpr,tpr,_ = roc_curve(y_test,y_proba)
    plt.plot(fpr,tpr,label=f"AUC = {roc_score:.2f}")
    plt.plot([0,1],[0,1],'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()

    return model

if __name__ == "__main__":
    train_model()
