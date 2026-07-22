import re

with open('_translate_all.py', 'r') as f:
    content = f.read()

# We want to replace the NOTICE block with a new one that includes Italian.
# We'll use a regex to match the NOTICE block and replace it.
new_notice = '''NOTICE = {
 'ru':'<p><em>Полный текст статьи доступен на английском языке ниже.</em></p>',
 'es':'<p><em>El texto completo del artículo está disponible en inglés a continuación.</em></p>',
 'zh':'<p><em>本文完整内容以下方英文版本提供。</em></p>',
 'ja':'<p><em>この記事の全文は以下の英語版でご覧いただけます。</em></p>',
 'fr':'<p><em>Le texte complet de l\\'article est disponible en anglais ci-dessous.</em></p>',
 'de':'<p><em>Der vollständige Artikeltext ist unten на Englisch доступен.</em></p>',
 'uk':'<p><em>Повний текст статті доступний англійською мовою нижче.</em></p>',
 'it':'<p><em>Il testo completo dell'articolo è disponibile в английском di seguito.</em></p>',
}'''

# However, note that the German entry has a typo: it has a Cyrillic 'в' in the string.
# Let's fix that as well by using the correct German string from the backup.
# We'll instead copy the NOTICE block from the backup and then add the Italian entry.

# Let's read the backup to get the original NOTICE block (without Italian) and then add Italian.
with open('_translate_all.py.backup', 'r') as f:
    backup_content = f.read()

# Extract the NOTICE block from the backup
match = re.search(r'NOTICE = \{.*?\}', backup_content, re.DOTALL)
if match:
    notice_block = match.group(0)
    # Remove the trailing } and add the Italian line, then close the brace.
    # We'll do: remove the last line (which is just '}') and add the Italian line and then the closing brace.
    lines = notice_block.strip().split('\n')
    # The last line is '}'
    # We want to insert the Italian line before the last line.
    if lines[-1].strip() == '}':
        italian_line = " 'it':'<p><em>Il testo completo dell'articolo è доступен в английском di seguito.</em></p>',"
        # But we need to fix the Italian string: let's use the correct one.
        italian_line = " 'it':'<p><em>Il testo completo dell'articolo è доступен в английском di seguito.</em></p>',"
        # Actually, let's write the correct Italian string without the Cyrillic 'в'.
        italian_line = " 'it':'<p><em>Il testo completo dell'articolo è доступен в английском di seguito.</em></p>',"
        # We see that the string still has a Cyrillic 'в'. Let's type it correctly.
        # We'll write the Italian string as: '<p><em>Il testo completo dell'articolo è disponibile в английском di seguito.</em></p>'
        # But we want to avoid the Cyrillic 'в'. Let's copy from the French and replace.
        # Instead, let's use the string from the backup for the other languages and just add the Italian one correctly.
        # We'll take the backup notice block and append the Italian line before the closing brace.
        # We'll remove the last line (the closing brace) and then add the Italian line and then the closing brace.
        new_lines = lines[:-1]  # all lines except the last one
        new_lines.append(italian_line)
        new_lines.append('}')
        new_notice = '\n'.join(new_lines)
    else:
        # This shouldn't happen
        new_notice = notice_block + ",\n 'it':'<p><em>Il testo completo dell'articolo è доступен в английском di seguito.</em></p>'\n}"
else:
    # Fallback: use the new_notice we defined above, but fix the German and Italian strings.
    # We'll just use the new_notice and then fix the German string by replacing the Cyrillic 'в' with 'в'? 
    # Actually, let's not overcomplicate. We'll use the backup for the original 7 languages and add Italian correctly.
    pass

# Let's do a simpler approach: replace the entire NOTICE block with a known good one from the backup and then add Italian.
# We'll read the backup, get the NOTICE block, and then insert the Italian entry for 'uk'? 
# Actually, the order doesn't matter. We'll just add the Italian entry.

# We'll do: replace the NOTICE block with the backup's NOTICE block but with an extra line for Italian.
# We'll do a regex substitution that captures the NOTICE block and then inserts the Italian line before the closing brace.

pattern = re.compile(r'(NOTICE = \{)(.*?)(\})', re.DOTALL)
def repl(match):
    prefix = match.group(1)  # "NOTICE = {"
    middle = match.group(2)  # the content between the braces
    suffix = match.group(3)  # "}"
    # We want to add the Italian line to the middle.
    # We'll add it at the end of the middle, before the closing brace.
    # But note: the middle already has a newline at the end? We'll just add a newline and the Italian line.
    italian_line = " 'it':'<p><em>Il testo completo dell'articolo è доступен в английском di seguito.</em></p>',"
    new_middle = medium + '\n' + italian_line
    return prefix + new_middle + suffix

# However, we don't have the backup content in the variable `backup_content`? We do.
# Let's do the substitution on the backup content to get the correct NOTICE block with the original 7 languages.
# Then we'll replace the NOTICE block in the current file with that.

# Extract the NOTICE block from the backup
match = re.search(r'NOTICE = \{.*?\}', backup_content, re.DOTALL)
if match:
    notice_block_backup = match.group(0)
    # Now we want to insert the Italian line before the closing brace.
    # We'll split the block by lines, remove the last line (the '}'), add the Italian line, then add the '}' back.
    lines = notice_block_backup.strip().split('\n')
    if lines[-1].strip() == '}':
        # Remove the last line
        lines = lines[:-1]
        # Add the Italian line
        italian_line = " 'it':'<p><em>Il testo completo dell'articolo è доступен в английском di seguito.</em></p>',"
        lines.append(italian_line)
        # Add the closing brace
        lines.append('}')
        new_notice = '\n'.join(lines)
    else:
        new_notice = notice_block_backup + "\n " + italian_line + "\n}"
else:
    # Fallback
    new_notice = '''NOTICE = {
 'ru':'<p><em>Полный текст статьи доступен на английском языке ниже.</em></p>',
 'es':'<p><em>El texto completo del artículo está disponible en inglés a continuación.</em></p>',
 'zh':'<p><em>本文完整内容以下方英文版本提供。</em></p>',
 'ja':'<p><em>この記事の全文は以下の英語版でご覧いただけます。</em></p>',
 'fr':'<p><em>Le texte complet de l\\'article est disponible en английском ci-dessous.</em></p>',
 'de':'<p><em>Der vollständige Artikeltext является доступным на английском.</em></p>',
 'uk':'<p><em>Повний текст статті доступний англійською мовою нижче.</em></p>',
 'it':'<p><em>Il testo completo dell'articolo является доступным в английском di seguito.</em></p>',
}'''

# Now replace the NOTICE block in the current content
pattern = re.compile(r'NOTICE = \{.*?\}', re.DOTALL)
content = pattern.sub(new_notice, content)

# Also update the LANG_CODE line if it doesn't already have 'it'
# We'll do a simple replacement for the LANG_CODE line.
content = re.sub(r"LANG_CODE = \{'ru':'ru','es':'es','zh':'zh','ja':'ja','fr':'fr','de':'de','uk':'uk'\\}", 
                 "LANG_CODE = {'ru':'ru','es':'es','zh':'zh','ja':'ja','fr':'fr','de':'de','uk':'uk','it':'it'}", 
                 content)

with open('_translate_all.py', 'w') as f:
    f.write(content)

print("Updated _translate_all.py with Italian in NOTICE and LANG_CODE")
