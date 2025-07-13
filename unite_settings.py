
import shutil
import argparse
import os

def parse_env_file(env_file='.env'):
    env_vars = {}
    with open(env_file, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                env_vars[key] = value.strip('"')
    return env_vars

def parse_args():
    env_vars = parse_env_file()
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, dest="path", default=env_vars.get('EVE_PATH'))
    parser.add_argument("--source_user_id", type=str, dest="source_user_id", default=env_vars.get('SOURCE_USER_ID'))
    parser.add_argument("--source_char_id", type=str, dest="source_char_id", default=env_vars.get('SOURCE_CHAR_ID'))
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    if not args.path or not os.path.exists(args.path):
        print(f"Eve path is invalid: {args.path}. Please provide a valid path.")
        return
    if not args.source_user_id or not args.source_char_id:
        print("Source user ID and character ID must be provided.")
        return
    
    with os.scandir(args.path) as entries:
        for entry in entries:
            if not entry.is_file() or not entry.name.endswith('.dat'): continue
            if '__' in entry.name: continue
            if entry.name.startswith('core_user_'):
                source_id = args.source_user_id
                prefix = 'core_user_'
            elif entry.name.startswith('core_char_'):
                source_id = args.source_char_id
                prefix = 'core_char_'
            else:
                continue

            bak_file = f"{entry.name}.bak"
            print(f"Backing up {entry.name} to {bak_file}")
            shutil.copyfile(os.path.join(args.path, entry.name), os.path.join(args.path, bak_file))

            source_file = f"{prefix}{source_id}.dat"
            if entry.name != source_file:
                print(f"Copying {source_file} as {entry.name}")
                shutil.copyfile(os.path.join(args.path, source_file), os.path.join(args.path, entry.name))

if __name__ == "__main__":
    main()