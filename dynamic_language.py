from cat.mad_hatter.decorators import hook


@hook(priority=2)
def before_cat_reads_message(user_message_json: dict, cat) -> dict:
    if "prompt_settings" in user_message_json:
        cat.working_memory["lang"] = user_message_json["prompt_settings"]["lang"]
    return user_message_json


@hook(priority=0)
def agent_prompt_suffix(suffix, cat):
    if "lang" in cat.working_memory:
        lang = cat.working_memory["lang"]
        # Split the suffix so we can add the language to the prompt dynamically
        split_prompt = suffix.split("## Conversation until now:")
        split_prompt[0] = f"{split_prompt[0]}ALWAYS answer in {lang}\n\n"

        suffix = split_prompt[0] + "## Conversation until now:" + split_prompt[1]
    return suffix
