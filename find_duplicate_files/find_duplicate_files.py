# Instead o fhashing the whotel contents of each ifle, we hashed three fixed-size "samples" for each file made out of the first x bytes, the middle i

# Solution:
# We walk through our whole file system iteratively. As we go, we take a "fingerprint" of each file in constant time by hashing the first few, middle few, and last few bytes
# We store each file's fingreprint in a has as we go

# If a given file's fingerprint is already in our hash, we assume we have a duplicate. In that case, we assume the file edited most recently is the one created by the friend

import os
import hashlib

def main():
    print(find_duplicate_files("./"))

def find_duplicate_files(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    # we'll track tuples of (duplicate_file, original_file)

    duplicates = []

    while len(stack):
        current_path = stack.pop()

        # if it's a directory,
        # put the contents in the stack

        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # if it's a file
        else:

            # get its hash
            file_hash = sample_hash_file(current_path)

            # get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen it before
            if file_hash in files_seen_already:

                existing_last_edited_time, existing_path = files_seen_already[file_hash]

                if current_last_edited_time > existing_last_edited_time:

                    # current file is the dupe!
                    duplicates.append((current_path, existing_path))

                else:
                    # old file is the dupe!
                    duplicates.append((existing_path, current_path))

                    # but also update files_seen_already to hvae the new file's info
                    files_seen_already[file_hash] = (current_last_edited_time, current_path)

            # if it's a new file, throw it in files_seen_already
            # and record its path and last edited time,
            # so we can tell later if it's a dupe

            else:
                files_seen_already[file_hash] = (current_last_edited_time, current_path)
                print(files_seen_already[file_hash])

    return duplicates

def sample_hash_file(path):

    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)

    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # if the file is too short to take 3 samples, hash the entire file

        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())
        
        else:
            num_bytes_between_samples = (total_bytes - num_bytes_to_read_per_sample * 3) / 2

            for offset_multiplier in xrange(3):
                start_of_sample = offset_multiplier * (num_bytes_to_read_per_sample + num_bytes_to_read_per_sample)
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()

if __name__ == "__main__":
    main()
