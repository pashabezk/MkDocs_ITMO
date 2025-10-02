import minify_html
import os
import rcssmin

TARGET_DIR = "site"


def minify_html_files():
	if not os.path.isdir(TARGET_DIR):
		print(f"Error: Target directory '{TARGET_DIR}' not found.")
		return

	print(f"Start HTML minification in directory '{TARGET_DIR}'...")

	total_files = 0
	modified_files = 0

	for dirpath, _, filenames in os.walk(TARGET_DIR):
		for filename in filenames:
			if filename.lower().endswith(('.html', '.htm')):
				total_files += 1
				file_path = os.path.join(dirpath, filename)

				try:
					with open(file_path, 'r', encoding='utf-8') as f:
						original_content = f.read()

					original_size = os.path.getsize(file_path)

					minified_content = minify_html.minify(original_content)

					with open(file_path, 'w', encoding='utf-8') as f:
						f.write(minified_content)

					new_size = os.path.getsize(file_path)
					reduction = (original_size - new_size) / original_size * 100 if original_size > 0 else 0

					print(f"  [OK] {file_path} (reduction: {reduction:.1f}%)")
					modified_files += 1

				except Exception as e:
					print(f"  [ERROR] processing {file_path}: {e}")

	print("\n-------------------")
	if total_files == 0:
		print(f"No HTML files found in '{TARGET_DIR}' or its subdirectories.")
	else:
		print(f"Operation complete! Files found: {total_files}. Successfully modified: {modified_files}.")


def minify_css_files():
	if not os.path.isdir(TARGET_DIR):
		print(f"Error: Target directory '{TARGET_DIR}' not found.")
		return

	print(f"Starting CSS minification in directory '{TARGET_DIR}'...")

	total_files = 0
	modified_files = 0

	for dirpath, _, filenames in os.walk(TARGET_DIR):
		for filename in filenames:
			if filename.lower().endswith('.css'):
				total_files += 1
				file_path = os.path.join(dirpath, filename)

				try:
					with open(file_path, 'r', encoding='utf-8') as f:
						original_content = f.read()

					original_size = os.path.getsize(file_path)

					minified_content = rcssmin.cssmin(original_content)

					with open(file_path, 'w', encoding='utf-8') as f:
						f.write(minified_content)

					new_size = os.path.getsize(file_path)
					reduction = (original_size - new_size) / original_size * 100 if original_size > 0 else 0

					print(f"  [OK] {file_path} (reduction: {reduction:.1f}%)")
					modified_files += 1

				except Exception as e:
					print(f"  [ERROR] processing {file_path}: {e}")

	print("\n-------------------")
	if total_files == 0:
		print(f"No CSS files found in '{TARGET_DIR}' or its subdirectories.")
	else:
		print(f"Operation complete! Files found: {total_files}. Successfully modified: {modified_files}.")


if __name__ == "__main__":
	minify_html_files()
	print("\n\n----------------------------------\n")
	minify_css_files()
