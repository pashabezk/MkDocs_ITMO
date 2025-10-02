import os
import htmlmin

TARGET_DIR = "site"


def minify_html():
	if not os.path.isdir(TARGET_DIR):
		print(f"Error: dir '{TARGET_DIR}' not found")
		return

	print(f"Start minification for '{TARGET_DIR}'...")

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

					minified_content = htmlmin.minify(
						original_content,
						remove_comments=True,
						remove_empty_space=True,
						reduce_boolean_attributes=True
					)

					with open(file_path, 'w', encoding='utf-8') as f:
						f.write(minified_content)

					new_size = os.path.getsize(file_path)
					reduction = (original_size - new_size) / original_size * 100 if original_size > 0 else 0

					print(f"  [OK] {file_path} (compression: {reduction:.1f}%)")
					modified_files += 1

				except Exception as e:
					print(f"  [ERROR] for {file_path}: {e}")

	print("\n-------------------")
	if total_files == 0:
		print(f"Dir '{TARGET_DIR}' and its sub dirs do not contains .html files")
	else:
		print(f"Minifying complete. Found files: {total_files}. Success files: {modified_files}")


if __name__ == "__main__":
	minify_html()
