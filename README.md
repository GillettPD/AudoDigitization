# README

# Guidelines for digitizing Mar Toma Audo's TREASURY OF THE SYRIAC LANGUAGE to `.json` format

Maxims for this project are:
- **Readability**. The `.json` file ought to have everything you need to make a readable version of the original printing to be deployed in digital contexts more easily than a PDF file.
- **Faithfulness**. This file should capture all of Audo's work as it was originally printed, barring minor details.
- **Searchability**. We want to be able to search the dictionary in a variety of ways. This will probably be the most important added value gained from this project.


## Layout of the entry

Headings are stored in a dictionary data structure, which is an **unordered data structure**. Technically speaking, the order that you enter each entry is not represented within the dictionary nor the `.json` file you save it to. In keeping with the **faithfulness** maxim, we want to reliaby store Audo's original entry ordering. This is enabled by storing each entry under a top-level key which is an *integer* rather than the actual heading in Syriac script. The `AudoMaker.py` script contains code which automatically finds the highest previous integer key and adds 1 to get the newest key. This means, first of all, that the work of digitizing the dictionary **needs to be entered into the `.json` file in the original order**. Don't hop around!

The value of each key is a nested dictionary with its own keys & values, containing all the actual content. These keys are:
- **letter** : Enter the Syriac-script initial letter of the entry. e.g. ܐ for ܐܵܠܲܦ
- **letter_order** : just in case we can't do an easy alphabetical sort of the entries by the actual bytes of Syriac script, put here an integer value representing the place that this entry falls in the order of the Syriac alphabet. For reference, the traditional order is    
    ܐ ܒ ܓ ܕ ܗ ܘ ܙ ܚ ܛ ܝ ܟ ܠ ܡ ܢ ܣ ܥ ܦ ܨ ܩ ܪ ܫ ܬ    
    read from left-to-right. A great mnemonic is    
        ܐܲܒܓܲܕ ܗܲܘܲܙ ܚܲܛܲܝ ܟܲܠܡܲܢ ܣܲܥܦܲܨ ܩܲܪܫܲܬ    
    For your convenience:    
    1. Alap. ܐ
    2. Beth. ܒ
    3. Gamal. ܓ
    4. Dalath. ܕ
    5. He. ܗ
    6. Waw. ܘ
    7. Zayn. ܙ
    8. Ḥeth. ܚ
    9. Ṭeth. ܛ
    10. Yod. ܝ
    11. Kap. ܟ
    12. Lamadh. ܠ
    13. Mim. ܡ
    14. Nun. ܢ
    15. Semkath. ܣ
    16. ʿE. ܥ
    17. Pe. ܦ
    18. Ṣadhe. ܨ
    19. Qop. ܩ
    20. Resh. ܪ
    21. Shin. ܫ
    22. Taw. ܬ
- **heading** : The entry, in Syriac script, which appears in large print in Audo's dictionary and which you would look up to find what you were looking for in a traditional dictionary. If Audo lists two or more variants immediately in the heading before the colon, only put the first form in this key.
- **heading_root** : Here, enter (as best you can) the consonantal root in Syriac script that the heading fits under; there should be no vowels or diacritics of any kind. Remove derivational suffixes, etc. 
- **definition** : Here, transcribe faithfully the entire entry in Syriac script. For convenience and consistency, make sure to *include the heading here*; start from the lemma and record everything until the subheadings or the next lemma, not omitting anything. Some notes on transcription:
    - Do not omit any diacritics that Audo included.
    - Variable-place diacritics such as *syame*, grammatical overdots & underdots, etc. should be included *somewhere* on the word, but you do not need to carefully copy Audo in this respect since the placement is immaterial (and anyways, the original printing sometimes does not have grammatical overdots etc. clearly above one or another letter). As a rule, put these marks last of all on the letter they combine with; i.e. after vowel & rukakha etc (see below).
    - When a letter has both a *qushaya* or *rukakha* mark and a vowel diacritic, place the former first and the latter second, and any variable-place diacritic last of all. For example, for ܐܲܒ݂ܵܐ you should type `\u0710\u0732\u0712\u0742\u0735\u0710` (with rukakha `\u0742`, *then* zqapa `\u0735` on beth) rather than `\u0710\u0732\u0712\u0735\u0742\u0710` and so on.
    - Place a space between a word any any punctuation that follows it. For example, write ܐܸܒܵܐ : ܐܸܒ݁ܒܵܢܹ̈ܐ (ܕܟܪ) ܗ̄ . ܕ̄ . ܦܹܐܪܵܐ and **not** ܐܸܒܵܐ: ܐܸܒ݁ܒܵܢܹ̈ܐ (ܕܟܪ) ܗ̄. ܕ̄. ܦܹܐܪܵܐ
- **subheadings** : Headings will often have subheadings, marked by a dash and indentation. These are stored in yet another nested dictionary whose key is `'subheadings'`. The keys and values of the nested dictionary are not a repeat of the higher level; here, simply put the subheading and its definition, if any. Some notes on best practices:
    - like headings, repeat the subheading itself in the definition; i.e. the key should be the initial one-word substring of the value. 
    - if a subheading has no definition, and is simply listed in the dictionary without any elaboration, leave the value as an empty string. 
    - if you find that Audo used a subheading mark to make some sort of remark or introduction to the next subheading, make it its own subheading as normal, but put the entire remark in the key and leave the value as an empty string. Also applies if he lists a word with ܘܫܪ܊ ("etc.") following and no further definition, see also the previous rule.
    - if there are no subheadings, you cannot enter an empty dictionary as the value. Instead replace it with an empty string, i.e. `'subheadings' = ""`

**Example**:
```python
update = {
    str(maxkey + 1) : {
        'letter' : "ܐ",
        'letter_order' : '1',
        'heading' : "ܐܲܒ݂ܵܐ",
        'heading_root' : "ܐܒܐ",
        'definition' : "ܐܲܒ݂ܵܐ : ܐܲܒ݂ܵܗܹ̈ܐ ܘܐܲܒ݂ܵܗܵܬ݂ܵܐ̈ (ܕܟܪ) ܗܵܘ̇ ܕܐܝܼܬ݂ ܠܹܗ ܚܲܕ݂ ܒܪܵܐ ܐܵܘ ܣܘܿܓ݂ܵܐܐ ܕܲܒ݂̈ܢܲܝܵܐ . ܡܸܬ݂ܐ̱ܡܲܪ ܐܵܦ ܥܲܠ ܚܲܝ̈ܘܵܬ݂ܵܐ . ܢܲܫܠܸܡ ܕܹܝܢ ܐܲܚܵܐ ܠܐܲܚܘܗܝ ܠܡܵܘܬܵܐ ܘܐܲܒ݂ܵܐ ܠܲܒ݂ܪܹܗ ܘܲܢܩܘܼܡܘܼܢ ܒ̈ܢܲܝܵܐ ܥܲܠ ܐܲܒ݂ܵܗܲܝ̈ܗܘܿܢ (ܨܘܪ) ܡܫܵܘܕ݁ܥܵܐ ܕܹܝܢ ܗܵܕ݂ܹܐ ܒܲܪ̄ܬ݂ ܩܵܠܵܐ ܐܵܦ ܥܲܠ ܩܲܫܝܼܫܵܐ ܐܵܘܟܹܝܬ݂ ܣܵܒ݂ܵܐ ܟܹܐܡܲܬ݂ ܐܲܒ݂ܵܐ ܕܐܲܒ݂ܵܐ . ܐܲܝܟ ܗܵܝ̇ : ܐܸܢܵܐ ܐ̄ܢܵܐ ܡܵܪܝܵܐ ܐܲܠܵܗܹܗ ܕܐܲܒ݂ܪܵܗܵܡ ܐܲܒ݂ܘܼܟ݂ . ܘܡܸܬ݂ܩܲܛ̱ܪܓ݂ܵܐ ܐܵܦ ܥܲܠ ܟܠܗܘܢ ܐܲܝܠܹܝܢ ܕܩܲܕ̣ܡܘܼܢ ܓܵܘܵܢܵܐܝܼܬ݂ . ܘܲܥ̣ܒ݂ܲܕ݂ ܐܵܣܵܐ ܕܫܲܦܝܼܪ ܩܕ݂ܵܡ ܡܵܪܝܵܐ ܐܲܝܟ ܕܵܘܝܼܕ݂ ܐܲܒ݂ܘܼܗܝ . ܐܲܒ݂ܵܗܲܝܢ̈ ܚ̣ܛܵܘ ܘܠܲܝܬ݁ ܐܸܢܘܿܢ (ܨܘܪ) . ܒܲܪ̄ܬ݂ ܩܵܠܵܐ ܕܐܲܒ݂ܵܗܹ̈ܐ ܡܫܵܘ̄ܕ݁ܥܵܐ ܥܲܠ ܐܲܒ݂ܵܐ ܘܐܸܡܲܪ ܐܲܟܲܚ̄ܕ݂ ܐܲܝܟ ܗܵܝ̇ : ܐܲܒ݂ܵܗܹ̈ܐ ܠܵܐ ܬܪܓ̇ܙܘܿܢ ܒܢܲܝ̈ܟ݁ܘܿܢ . ܐܲܒܵܗܵܬ݂ܵܐ̈ ܝܲܬ݁ܝܼܪ ܕܲܠܝܼܠܵܐ ܗ̄ܝ̣ ܒܲܚܫܲܚܬ݂ܵܐ ܡ̣ܢ ܐܲܒ݂ܵܗܹܐ̈ . ܩܲܒ݂ܪܘܼܗܝ ܥܲܡ ܐܲܒ݂ܵܗܵܬܹ̈ܗ ܒܲܩܪܝܼܬ݂ܐ ܕܕܵܘܝܼܕ݂ . ܘܡܸܬ݂ܚܲܙܝܵܐ ܕܐܲܒ݂ܵܗܹ̈ܐ ܥܕܲܡܵܐ ܠܥܸܣܪܵܐ . ܘܐܲܒ݂ܵܗܵܬ݂ܵܐ̈ ܠܥܸܠ ܡ̣ܢ ܥܸܣܪܵܐ ܐܸܢ ܝܲܬ݁ܝܼܪܝܼܢ . ܡܫܵܘܕ݁ܥܵܐ ܬܘܼܒ݂ ܒܲܪ̄ܬ݂ ܩܵܠܵܐ ܕܐܲܒ݂ܵܐ ܥܲܠ ܪܹܫܵܐ  ܕܫܲܪܒ݁ܬ݂ܵܐ ܡܬ݂ܝܼܚܬܵܐ ܘܐܲܪܝܼܟ݂ܬܵܐ ܐܲܝܟ ܗܵܝ̇ : ܪܹܫ ܐܲܒ݂ܵܗܵܬ݂ܵܐ̈ ܕܵܘܝܼܕ݂ (ܨܘܪ) ܘܥܲܠ ܗܵܘ̇ ܕܡܸܬ݁ܕ݁ܲܒܲܪ ܥܲܡ ܐ̄ܚܪ̈ܵܢܹܐ ܐܲܝܟ ܐܲܒ݂ܵܐ . ܐܲܒ݂ܵܐ ܕܝܲܬ݂ܡܹ̈ܐ ܘܕܲܝܵܢܵܐ̇ ܕܐܲܪ̈ܡܠܵܬ݂ܵܐ . ܘܥܲܠ ܥܵܒ݂̇ܘܿܕ݂ܵܐ ܘܡܲܬ݂ܩܢܵܢܵܐ ܘܲܡܣܲܬ݁ܪܵܢܵܐ . ܘܥܲܠ ܐܲܠܵܗܵܐ : ܐܲܒ݂ܘܼܢ ܕܒ݂ܲܫܡܲܝܵܐ . ܕܲܠܡܵܐ ܠܵܐ ܗ̄ܘ̣ܵܐ ܐܲܒ݂ܘܼܟ݂ ܕܲܩ̣ܢܵܟ݂ ܘܫܪ܊ . ܘܥܲܠ ܡܲܠ̈ܦܵܢܹܐ ܕܥܹܕܬ݁ܵܐ : ܐܲܒ݂ܵܐ ܕܐܲܒ݂ܵܗܵܬ݂ܵܐ̈ . ܗ̄ . ܕ̇ . ܦܲܛܪܝܼܵܪܟܵܐ . ܒܹܝܬ݂ ܐܲܒ݂ܵܗܵܬ݂ܵܐ̈ . ܗ̄ . ܕ̄ . ܩܸܠܵܝܬܵܐ ܦܲܛܪܝܼܵܪܟܵܝܬܵܐ . ܒܢܲܩܝܼܦܘܼܬ݂ ܚܠܵܦ ܫܡܵܐ ܣܒ݂ܝܼܣܵܐ ܠܗܵܕ݂ܹܐ ܒܲܪ̄ܬ݂ ܩܵܠܵܐ ܥܵܐ̇ܠܵܐ ܘܵܐܘ ܪܒ݂ܝܼܨܬܵܐ ܩܕ݂ܵܡ ܚܠܵܦ ܫܡܵܐ ܐܲܝܟ ܐܲܒ݂ܘܼܟ݂ ܐܲܒ݂ܘܼܗܝ ܘܫܪ܊ . (ܚܙܝܼ ܓܪܲܡܡܵܛܝܼܩܝܼ) .", # note that the heading is repeated in the definition
        'subheadings' : {
            "ܐܲܒ݂ܵܗܘܼܬ݂ܵܐ" : "ܐܲܒ݂ܵܗܘܼܬ݂ܵܐ . ܐܲܒ݂ܵܗ̈ܘܵܬ݂ܵܐ (ܢܩܒ)", # note again that the subheading is repeated in its definition
            "ܐܲܒ݂ܵܗܵܝܵܐ" : "ܐܲܒ݂ܵܗܵܝܵܐ . ܐܲܒ݂ܵܗܵܝܹ̈ܐ . ܐܲܒ݂ܵܗܵܝܬܵܐ ܘܫܪ܊ . ܡ̣ܢ ܐܲܒ݂ܵܗܵܬ݂ܵܐ̈ ܠܲܝܬ݁ ܒܲܝܬܵܝܘܼܬ݂ܵܐ",
            "ܐܲܒ݂ܵܗܵܐܝܼܬ݂" : "", # example of a one-word subheading
            "ܘܡܸܬܚܲܫܠܵܐ ܡ̣ܢ ܒܲܪ̄ܬ݂ ܩܵܠܵܐ ܕܐܲܒ݂ܵܐ : ܡܸܠܬ݂ܵܐ :" : "", # example of a remark in a subheading slot
            "ܐܲܒܲܗ" : "ܐܲܒܲܗ . ܗ̄ . ܕ̄ . ܥܲܒ݂ܕܹ݁ܗ ܐܲܒ݂ܵܐ . ܘܐܸܬܐܲܒܲܗ ܐܵܘ ܐܸܬܐܲܒ݂ . ܗ̄ . ܕ̄ . ܗ̤ܘܵܐ ܐܲܒ݂ܵܐ ܘܫܲܪܟܵܐ ܕܣܘܼܪ̈ܥܵܦܲܝܗܹܝܢ"
        }
    }
}
```