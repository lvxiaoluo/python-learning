import os
import glob

# Directory path
directory = r"D:\maintenance\VW\需求跟进\PNS\000000000A7C573A_LSVDN6C45SN039142-20251020185001_546-165-result\aplogcat"

# Keyword to search for
# keyword = "h5_call_native_get_current_pos"
keyword = "初始化地图报错"

# List to store filenames containing the keyword
matching_files = []

# Check if directory exists
if not os.path.exists(directory):
    print(f"Directory does not exist: {directory}")
    exit(1)

# Find all .txt files in the directory
txt_files = glob.glob(os.path.join(directory, "*.txt"))

print(f"Found {len(txt_files)} txt files in directory")

# If no txt files found
if not txt_files:
    print("No .txt files found in the directory")
    exit(1)

# Show first few files for verification
print("First 5 files found:")
for i, file_path in enumerate(txt_files[:5]):
    print(f"  {i+1}. {os.path.basename(file_path)}")

# Iterate through all .txt files
files_processed = 0
for file_path in txt_files:
    files_processed += 1
    if files_processed % 10 == 0:  # Progress indicator
        print(f"Processed {files_processed}/{len(txt_files)} files...")
    
    try:
        # Get file size
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            print(f"Skipping empty file: {os.path.basename(file_path)}")
            continue
            
        # Try different encodings
        content = None
        for encoding in ['utf-8', 'gbk', 'latin-1']:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    content = file.read()
                    break  # Successfully read the file
            except UnicodeDecodeError:
                continue  # Try next encoding
        
        # If all encodings failed, try with error handling
        if content is None:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
        
        # Check if keyword exists in the file content
        if keyword in content:
            matching_files.append(os.path.basename(file_path))
            print(f"Found keyword in: {os.path.basename(file_path)}")
        #else:
            # Uncomment below line for debugging - shows files without keyword
            #print(f"Keyword not found in: {os.path.basename(file_path)}")
                    
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

# Output the matching filenames
print("\n" + "="*50)
if matching_files:
    print("Files containing the keyword:")
    for file in matching_files:
        print(file)
else:
    print("No files contain the keyword.")
    print("\nPossible reasons:")
    print("1. The keyword might not exist in any files")
    print("2. The keyword might have different case (try case-insensitive search)")
    print("3. The keyword might be split across lines")
    print("4. Files might be in a different format than expected")