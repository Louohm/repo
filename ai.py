import pandas as pd
import os

def main():
    # Define the filename
    data_path = 'sample_data.csv'
    
    print("🚀 AutoInsight: Starting Analysis...")
    
    # Checkpoint 1: Directory Check
    current_dir = os.getcwd()
    print(f"📂 Currently looking in: {current_dir}")

    # Checkpoint 2: File Existence Check
    if not os.path.exists(data_path):
        print(f"❌ ERROR: '{data_path}' not found in the current folder.")
        print("💡 TIP: Move your CSV file into this folder or use 'cd' to navigate here.")
        return

    try:
        # Checkpoint 3: Load Data
        df = pd.read_csv(data_path)
        print(f"✅ Successfully loaded '{data_path}'")
        print(f"📊 Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

        # --- Analysis Logic ---
        
        # Identify numeric columns
        numeric_cols = df.select_dtypes(include='number').columns
        
        if len(numeric_cols) == 0:
            print("⚠️ No numeric columns found to analyze.")
            return

        # Correlation analysis
        corr_matrix = df[numeric_cols].corr()
        print("📈 Correlation Matrix:")
        print(corr_matrix)

        # Find strongest correlations (excluding self-correlation)
        strong_corrs = [(i, j, corr_matrix.loc[i,j])
                        for i in numeric_cols for j in numeric_cols
                        if i != j and abs(corr_matrix.loc[i,j]) > 0.7]

        if strong_corrs:
            print("\n🔥 Strong correlations (>0.7) found:")
            for i, j, val in strong_corrs:
                print(f"   - {i} and {j}: {val:.2f}")
        else:
            print("\nℹ️ No strong correlations found.")

        # Generate quick textual insights
        print("\n💡 Key Insights:")
        for col in numeric_cols:
            mean_val = df[col].mean()
            print(f"   - The average of {col} is {mean_val:.2f}.")

        print("\n✨ Analysis complete!")

    except Exception as e:
        print(f"💥 An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
