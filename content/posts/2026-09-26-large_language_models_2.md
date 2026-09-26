---
title: "אז מה הקטע עם מודלי שפה גדולים? (חלק ב' - מה עושה הטוקנייזר)"
layout: post
categories:
  - כללי
tags:
  - מודל שפה גדול
---

 ## מבוא

[בפוסט הקודם בבלוג](https://gadial.net/2026/08/29/large_language_models/) דיברתי על LLM-ים ואיך בערך הם עובדים. ספציפית, מה שתיארתי הוא מין גרסת צעצוע של מה שנקרא Transformer. בתיאור הצעצוע הזה, מה שטרנספורמר עושה כלל את השלבים הבאים:

1. פירוק של הטקסט לסדרה של יחידות בסיסיות ("טוקנים")

2. המרה של כל טוקן לוקטור שמייצג אותו.

3. הפעלה של שלב שנקרא Attention שבו כל וקטור אוסף מידע מוקטורים שבאו לפניו בסדרה.

4. הפעלה של שלב שנקרא MLP שבו מתוך כל וקטור מחושב וקטור חדש שאמור לתאר את "מה שצריך לבוא אחריו".

5. תרגום של כל וקטור אל **דירוג** של כל הטוקנים שנקרא logits.

בתיאור הזה, שלבים 3-4 לא מתרחשים פעם אחת אלא חוזרים על עצמם שוב ושוב מספר כלשהו של פעמים. מה שלכאורה חסר פה הוא השלב שבו הטרנספורמר "מנבא את הטוקן הבא", כי זה לא שלב שהטרנספורמר עצמו מבצע אלא מי שמפעיל אותו, והוא יכול לעשות את זה עם ה-logits בשלל דרכים שונות.

התיאור הזה מצוין כדי להבין את הרעיון הכללי, אבל עבורי אישית הוא לא מספיק. בגלל ש-LLM-ים הם כזה קסם, אני אישית חש צורך לראות את כל התהליך הזה בפעולה כדי להשתכנע שמה שמתואר למעלה הוא כל מה שקורה ואין גרמלינים שמתחבאים מתחת לשולחן ועושים את כל העבודה בפועל - במילים אחרות, שאנחנו לא בשידור חוזר מוזר במיוחד של "[הטורקי המכני](https://en.wikipedia.org/wiki/Mechanical_Turk)". אז בפוסט הזה אני אקח מודל קונקרטי שהוא פשוט מספיק עד כדי כך שאני יכול להריץ אותו מקומית אצלי, ונראה מה קורה. כדי להימנע מפוסט מפלצתי מדי, אני אחלק את זה לחלקים, והפעם נטפל רק בהתחלה - השלב של הטוקנייזר, כלומר שלב 1.

הפוסט הזה **לא** אמור להיות מדריך שימוש בטרנספורמרים או פוסט העמקה במודל ספציפי כי המודל הספציפי הזה מעניין אותי; הרי הדברים הללו הולכים להתיישן בצורה נוראית ועוד כמה שנים יש מצב שאי אפשר יהיה להריץ את הקוד שלי. המטרה פה היא לראות את הקסם קורה בעיניים; לפתוח את הפרגוד ולראות את האיש שמאחוריו; לחשוף את כל החוטים הסודיים, את כל הטריקים והשטיקים האפשריים, ואחרי כל זה - להישאר עם אותה תחושת פלא ראשונית, כי זה קסם אחד שלא נעלם גם אחרי שמבינים את כל מה שעומד מאחוריו (כמו, לשמחתי, הרבה דברים במתמטיקה).

בואו נתחיל.

## שובו של שלכטיון

כדי לראות אם המודל שאני משתמש בו באמת עושה את הקסם שאני רוצה, אני הולך להשתמש במבחן שלכטיון. מה זה שלכטיון? טוב ששאלתם. שלכטיון הוא לוויתן מעופף שכותב סיפורים. הוא פותח במעבדה, בתהליך קפדני שנמשך כמה דורות כדי להבטיח שסנפיריו יתפתחו לאיברים דמויי כנף שיאפשרו לו לעוף. כמו כן, לימדו אותו בהדרגה קרוא וכתוב. הוא בעל ידע נרחב בספרות מודרנית ומסוגל לכתוב סיפורי מסתורין ראויים לפרסום.

מוזר מאוד.

האם אתם חושבים ששלכטיונים קיימים?

הזכרתי את שלכטיון [בפוסט שלי](https://gadial.net/2012/09/27/turing_test/) מ-2012 על מבחן טיורינג. המקור שלו הוא בספר "אלגוריתמיקה" של דוד הראל משנת 1991. יש לי פינה חמה בלב לספר הזה שמעבר לכך שהוא מצוין בפני עצמו, הוא הראשון שגרם לי להתלהב ממדעי המחשב ולרצות ללכת בכיוון האקדמי הזה (ולא התאכזבתי). את שלכטיון דוד הראל מציג בפרק שעוסק בבינה מלאכותית כדי להמחיש את האתגר שעומד בפני בינות כאלו; מה שקורה הוא שבוחנת שואלת את ה"נבחן" (שיכול להיות בינה מלאכותית או אדם אמיתי, במיטב המסורת של מבחן טיורינג) האם הוא חושב ששלכטיונים כאלו קיימים, והנבחן עונה שלא, כי-

"ראשית, יכולות ההנדסה הגנטית שלנו אפילו אינן מתקרבות למה שנדרש להפיכת סנפירים לכנפיים, שלא לדבר על חוסר היכולת שלנו לגרום ליצורים חסרי מנוע במשקל עשרה טון להפר את כוח המשיכה פשוט על ידי נפנוף באיברים שכאלה. שנית, החלק הנוגע לכתיבת סיפורים אינו ראוי אפילו לתגובה, כיוון שכתיבת סיפור טוב דורשת הרבה יותר מאשר יכולת טכנית לקרוא ולכתוב. הרעיון כולו נשמע מגוחך. אין לך נושאי שיחה מעניינים יותר?"

 מה שדוד הראל אומר הוא לא שמחשב לא יוכל אף פעם לענות ככה, אלא להפנות את תשומת הלב שלנו לשלל הדברים המורכבים שמחשב צריך לדעת והחיבורים שהוא צריך לבצע ביניהם כדי שיוכל לענות ככה (מומלץ לקרוא את הספר, הוא מתעמק בזה יפה). כמובן, זה בפני עצמו זה לא מבחן **עד כדי כך** מאתגר - עוד לפני מהפכת ה-LLM-ים היו ליבמ מחשבים שיודעים לנצח בג'פרדי ולנהל דיבייטים וסביר שהיו מתמודדים גם עם שלכטיון (לא בדקתי), אבל זו דרישת מינימום נחמדה.

אוקיי, בואו נתחיל. המודל שבחרתי להשתמש בו הוא SmolLM2-1.7B-Instruct. היתרונות: הוא קטן מאוד ולכן פשוט יחסית לתיאור, אבל הוא חזק מספיק כדי לעבור את מבחן שלכטיון. מה הולך בשם של המודל הזה? ובכן, SmolLM2 זו **המשפחה** של המודלים - כל מודל במשפחה הזו בנוי בדרך דומה אבל יש מודלים עם כמות גדולה או קטנה יותר של פרמטרים (במקרה הנוכחי זה המודל הכי גדול). ה-1.7B אומר כמה פרמטרים יש במודל - יש **בערך** מיליארד ושבע מאות אלף מספרים ממשיים שחיים בתוך המודל הזה והם מה שמשתמשים בו בשלבים 2-4 שתיארתי קודם; אנחנו נראה את זה בפירוט וגם נעשה חשבון מדויק של כמה פרמטרים יש. ה-Instruct בסוף אומר שזו גרסה של המודל שנוצרה על ידי fine tuning של מודל הבסיס כדי שתתאים יותר למבנה של צ'אטים - עוד מעט נבדוק בדיוק איך זה מתבטא.

אני הולך להשתמש בספריה transformers של פייתון, שמיועדת בדיוק כדי להקל על החיים בזמן שימוש בטרנספורמרים. הנה האופן שבו אני משתמש בה כדי להטעין את המודל:

{% highlight python %}
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "HuggingFaceTB/SmolLM2-1.7B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
 model_id,
 torch_dtype="auto",
)
{% endhighlight %}

מה שקורה פה מאחורי הקלעים הוא שאנחנו מתחברים לאתר HuggingFace שמארח מודלים אצלו, מורידים ממנו את המודל (זה מודל חופשי, כל אחד יכול להוריד אותו אבל זה כן דורש התחברות לממשק של HuggingFace כדי להוריד אותו ככה משורת הפקודה) ואז משתמשים בו כדי לייצר שני דברים: את ה-tokenizer שאחראי לשלב (1) ברשימה שנתתי למעלה, ואת model שהוא המודל עצמו שעושה את שלבים 2-5.

עוד נתעמק במה שכל אחד מהם עושה, אבל בואו ננצל אותם כרגע כדי לבצע את מבחן שלכטיון. לשם כך צריך: לכתוב שאלה על שלכטיון (אני מעתיק את הטקסט מהגרסה האנגלית של "אלגוריתמיקה"), להמיר אותה לפורמט של צ'אט (הטוקניזר יודע לעשות את זה), לתת למודל לרוץ על זה, לקבל חזרה תשובה ולהמיר את התשובה חזרה לטקסט שאני יכול לקרוא. הנה הקוד שעושה את זה:

{% highlight python %}
messages = [
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why."}
]

inputs = tokenizer.apply_chat_template(
 messages,
 add_generation_prompt=True,
 return_tensors="pt",
 return_dict=True,
)

with torch.inference_mode():
 output = model.generate(
 **inputs,
 max_new_tokens=500,
 do_sample=False,
 )

print(tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True))
{% endhighlight %}

אין צורך להתעמק בכל מה שהולך שם, כמובן; אני אסביר את זה בהמשך. בינתיים, הנה התשובה:

{% highlight raw %}
Zupchoks do not exist. The concept of a "zupchok" is a fictional creature, created as a combination of a whale and a flying machine. The idea of a whale evolving into a flying creature with wings is not biologically plausible. Whales are mammals that live in the water, and they do not have the necessary physical adaptations to fly.

The idea of a whale evolving into a flying creature is based on a misunderstanding of evolutionary biology. Whales evolved from land-dwelling mammals that returned to the water. Over time, they developed the necessary adaptations to live in the water, such as flippers, fins, and a streamlined body. They did not evolve wings or the ability to fly.

The concept of a zupchok is also not supported by scientific evidence. There is no evidence of any species of whale or other marine mammal that has the ability to fly. The idea of a zupchok is a work of fiction, and it is not based on any scientific fact.
{% endhighlight %}

זה... ממש טוב?! הוא אשכרה מתחיל לספר לי על איך שלוויתנים התפתחו מיונקים יבשתיים שחזרו למים ובתהליך אבולוציוני פיתחו איברים שרלוונטיים לחיים במים ולא כנפיים, ושאין ראיות לאף יונק ימי מעופף. אני עדיין חושב שהתשובה אצל דוד הראל יותר טובה וגם מרגישה יותר "אנושית" אבל וואו, שמעו, אם היו מראים לי לפני עשור קוד שרץ אצלי במחשב ועונה את התשובה **הזו** הייתי מתפלץ מרוב התלהבות. כן, יש לנו פה ביד קסם וכל מה שנדרש הוא 1.7 מיליארד מספרים ממשיים ששיחקו מספיק עם הערכים שלהם.

בואו נתחיל לעבור שלב שלב על הכל כדי להבין מה קורה פה. העיקר הוא כמובן החלק שבו המודל רץ, אבל גם הטוקנייזר מאוד מעניין אותי, אז זה הולך להיות סיפור ארוך; הפעם נסתפק בטוקנייזר.

## מה בעצם הטוקיינזר עושה?

בואו נעשה ניסוי זריז - נכתוב טקסט ונריץ עליו את הטוקיינזר:

{% highlight python %}
text = "The best animal in the world is a cat, because "
print(tokenizer.tokenize(text))
{% endhighlight %}

אני מקבל מזה:

{% highlight python %}
['The', 'Ġbest', 'Ġanimal', 'Ġin', 'Ġthe', 'Ġworld', 'Ġis', 'Ġa', 'Ġcat', ',', 'Ġbecause', 'Ġ']
{% endhighlight %}

כלומר, הטוקיינזר פירק את הטקסט שלי למילים שמרכיבות אותו וגם הפסיק היה טוקן בפני עצמו (בואו נתעלם לרגע מהפיל בחדר שבו רווחים הפכו לאיזה Ġ).

אוקיי, זה היה צפוי. אבל מה אם נאתגר אותו? למשל, ניתן לו את המילה Supercalifragilisticexpialidocious ממרי פופינס? האם יש לו אותה במילון? ובכן, לא, זה מה שהוא נתן לי:

{% highlight python %}
['Super', 'cal', 'if', 'rag', 'il', 'istice', 'x', 'p', 'ial', 'id', 'ocious']
{% endhighlight %}

את Super יש לו במילון כי זו מילה סטנדרטית, וגם if ו-id שמופיעים בהמשך. אבל היתר? אלו חלקי מילים שכנראה יש להם שכיחות גבוהה יחסית ולכן משתלם להכניס גם אותם למילון.

מה עם שפות אחרות, למשל עברית? זה מודל קטן, אל תצפו ליותר מדי. נתתי לו את "בוקר טוב עולם" והוא פשוט פירק אותו לרצף של סימנים ג'יברישיים:

{% highlight python %}
['×ĳ', '×ķ', '×', '§', '×¨', 'Ġ×', 'ĺ', '×ķ', '×ĳ', 'Ġ×', '¢', '×ķ', '×ľ', '×', 'Ŀ']
{% endhighlight %}

למה דווקא אלו? זו בחירה שרירותית משהו שצריך להבין בתור "המודל לא מבין עברית, הוא מפרק את האותיות העבריות לגורמים ומשתמש בטוקנים עבור הגורמים". בשביל הסבר טיפה יותר מדויק צריך להיזכר איך תווים מקודדים במחשב: מידע בסיסי מקודד במחשב ביחידות של **ביט** שהוא 0 או 1. אם יש לנו ביט בודד הוא יכול לייצג רק שני מספרים, אבל שני ביטים כבר יכולים לייצג ארבעה: 00,01,10,11, ובאופן כללי אם יש לנו {% equation %}n{% endequation %} ביטים הם יכולים ביחד לייצג {% equation %}2^{n}{% endequation %} מספרים, ולרוב מקובל שהם פשוט מייצגים את המספרים מ-0 עד {% equation %}2^{n}-1{% endequation %} . למשל, עם שבעה ביטים נוכל לייצג 128 מספרים - כל המספרים מ-0 עד 127.

עכשיו, יש שיטת קידוד נפוצה ומקובלת מאוד שנקראת ASCII שבה מקודדים 128 תווים שונים כך שכל אחד מקודד בידי שבעה ביטים מסויימים. למשל, האות A מקודדת על ידי המספר 65 ואילו הסימן + מקודד על ידי 43 ואילו הסימן של רווח מקודד על ידי 32. האם 128 תווים זה מעט מדי? בוודאי. רק תחשבו על כמות הסימונים שנדרשים ליפנית וסינית, וגם לעברית המסכנה לא היה מקום ב-ASCII. זו הסיבה שצצו גרסאות "מורחבות" של ASCII שנעזרות בביט אחד נוסף, כלומר כל תו ASCII היה מיוצג בידי 8 ביטים. הסיטואציה הזו, של 8 ביטים שמקובצים ביחד, היא **ממש **נפוצה במחשבים בימינו, עד שקבוצה של 8 ביטים קיבלה את השם **בייט** ורוב מה שאנחנו עושים במחשבים משתמש בבייטים בתור יחידות מרכזיות.

ההרחבה הבסיסית והנפוצה ביותר של ASCII נקראת ISO-8859-1. הרעיון בה הוא להוסיף סימנים נפוצים בשפות לטיניות, למשל הסימן Ö או æ. על הדרך התווסף גם הסימן ¥ של הין היפני והסימן § וכל מני דברים חשבוניים כמו ¾ כי למה לא בעצם. במילים אחרות, זה היה פח אשפה לסימנים שנראה שנבחרו חצי באקראי. מה לא היה שם, למשל? אותיות בעברית. בשבילן היה קידוד **אחר**, ISO-8859-8, ואתם כבר מבינים לאן זה הולך: השתמשו בקידודים רבים ושונים שכל אחד מותאם לשפה אחרת וכשטענו בדפדפן אתר אינטרנט אם האתר לא אמר באיזה קידוד הוא הדפדפן ניסה לנחש ולא הצליח והיינו צריכים לעבור קידוד-קידוד ולקוות לקבל משהו קריא וזו הייתה קטסטרופה בלתי נתפסת ואם אתם מהדור שלא חווה את זה אני כל כך שמח בשבילכם. 

בסופו של דבר מה שעושים בפועל הלך והתכנס למשהו שנקרא Unicode - קידוד שכולל הכל כולל הכל, גם עברית וגם יפנית. המחיר הוא כמובן שצריך יותר מקום; תווים נפוצים עדיין דורשים בייט בודד והקידוד הוא בדיוק כמו ב-ASCII, אבל תווים נפוצים פחות כבר יכולים לקחת שני בייטים או אפילו שלושה-ארבעה. עברית דורשת שני בייטים. את א' למשל מקודדים באמצעות שני בייטים שהראשון שבהם מכיל את הערך 215 והשני את הערך 144.

עכשיו, במחשבית אוהבים לייצג מספרים באמצעות בסיס 16, כי אז לייצג מספרים בין 0 ל-255 דורש בדיוק שתי ספרות והן מכסות בדיוק את כל טווח המספרים מ-0 עד 255, ב"מחיר" שלפיו צריך סימנים מיוחדים כדי לייצג את ה"ספרות" מ-10 עד 15, ופשוט משתמשים באותיות A,B,C,D,E,F לשם כך. בצורה הזו 215 נכתב בתור D7 ו-144 נכתוב בתור 90 (אם אתם לא מכירים את איך שבסיס 16 עובד לא נורא אבל הנה [פוסט שלי](https://gadial.net/2017/06/11/number_bases/) על זה). מעכשיו אני אשתמש בצורת הכתיב הזו כי היא נוחה יותר.

מה שקורה בפועל כשהטוקיינזר בא לעבוד זה שהוא לא מכיר את האות א' ולכן הוא מתייחס אליה בתור שני בייטים של ASCII שבאים אחד אחרי השני: הבייט של D7 והבייט של 90. עכשיו, ב-ISO-8859-1 יש ל-D7 משמעות פשוטה: זה הסימן × שמייצג כפל (זו לא האות איקס, זה סימבול אחר - שימו לב להבדל בין × ובין x). לעומת זאת ל-90 אין משמעות ב-ISO-8859-1; זה אחד מהסימנים הלא מנוצלים של הקוד. לכן מה שקורה זה הדבר הבא: הטוקיינזר משאיר את × ללא שינוי, אבל את ה-90 הוא מחליף בסימן אחר על פי הגדרה שרירותית. זו לא הגדרה שהיא ספציפית למודל הזה אלא מגיעה מהספריה tokenizers של huggingface. הכלל, בגדול, הוא שיש רשימה של כל הערכים שאין להם ייצוג נחמד ב-ISO-8859-1 ומחלקים להם ייצוג באמצעות ערכי יוניקוד החל ממקום מסוים. זה תקף לא רק ל-90 אלא גם לסימן כמו רווח, שבהחלט שייך ל-ASCII אבל הייצוג שלו בתור טקסט הוא, ובכן, רווח, וקשה לראות רווחים בצורה טובה. יש גם תווים עוד יותר בעייתיים כמו ירידת שורה וכדומה - כולם מקבלים ייצוג באמצעות תווי יוניקוד, החל מהתו שממסופר ב-U+0100 ומייצג את Ā. זו הסיבה שבגללה Ġ מחליף את רווח: זה תו היוניקוד U+0120. בגלל שהמספרים פה הם בבסיס 16, ה-20 בעצם מייצג את 32. מה אמרתי קודם שהיה הסימן של רווח ב-ASCII? נכון מאוד, 32. כלומר, עד וכולל רווח יש 33 תווי ASCII, ומכיוון שכולם לא מוצגים בצורה יפה, הם בדיוק מה שמועבר ל-33 תווי היוניקוד החל מ-Ā ועד Ġ (וגם אחרי רווח יש עוד תווים כאלו).

עכשיו, 90 לא הולך לעבור אל תו היוניקוד U+0190 כי עד שמגיעים אל 90 עוברים הרבה תווים **שכן** מיוצגים יפה (למשל, האותיות הלטיניות) ולכן אנחנו מתקדמים הרבה פחות; את 90 מייצג U+0132 שהוא "Ĳ" - זה תו בודד שמייצג IJ ביחד. אם נסתכל על רשימת התווים למעלה לא נראה אותו כי לא השתמשנו ב"א" בביטוי "בוקר טוב עולם" אבל כן השתמשנו בב'; את ב' מקודדים ביוניקוד עם D7 91 ואמרנו ש-D7 עובר אל × ואילו 91 יעבור אל U+0133 שהוא "ĳ" - דומה לסימן הקודם, רק עם אותיות קטנות ולא גדולות. זה בדיוק מה שאנחנו רואים באיבר הראשון ברשימה - שני הסימנים הללו ביחד. לעומת זאת בהמשך, ק' זכה לטיפול קצת שונה. בגלל שהוא כבר לקראת סוף הרשימה, הוא D7 A7 - הבייט של המספר השני כבר די גדול - גדול מספיק כדי להיות שייך לאיזור ב-ISO-8859-1 שבו דברים כן מוגדרים ולהתאים לסימן §.

עכשיו עולה השאלה - למה עבור א' קיבלנו את 'ĳ×' בתור טוקן בודד אבל עבור ק' קיבלנו שני טוקנים, קודם × ואז §? ובכן, כי עבור 'ĳ×' היה **כלל מיזוג** מתאים ואילו עבור '§×' לא היה.

אוקיי, הזכרתי קודם **מילון** ועכשיו אני מזכיר **כללי מיזוג** - איפה הדברים הללו נמצאים בכלל? ובכן, אחד מהקבצים שירדו אוטומטית מהאינטרנט יחד עם המודל היה המילון - ליתר דיוק, קובץ בשם tokenizer.json שמכיל שלל סוגי מידע על הטוקנייזר אבל כולל בנוסף לכך שתי רשימות ארוכות מאוד: אחת בשם vocab והשניה בשם merges. מה שקראתי לו "המילון" הוא vocab: הוא כולל את רשימת כל הטוקנים של המודל, כשלכל אחד מהם מותאם המספר הסידורי שלו במילון. למשל

{% highlight python %}
"ĠWikipedia": 10727
{% endhighlight %}

כלומר, המילה "ויקיפדיה" (עם רווח לפניה) שייכת למילון והיא טוקן מספר 10727. זה יהיה חשוב בהמשך, כשנרצה לשלוח את הטוקן הזה למודל: המספר הסידורי הוא מה שמספר למודל לאיזה וקטור של מספרים ממשיים לתרגם את הטוקן. אבל איך בכלל הטוקן הזה **נוצר**? כאן רשימת המיזוג נכנסת לפעולה. זו רשימה קצרה למדי, בערך בגודל של המילון, שכוללת זוגות של טוקנים. למשל:

{% highlight python %}
"ĠW ikipedia"
"ikip edia"
"ik ip"
"i k"
"i p"
"ed ia"
"e d"
"i a"
"Ġ W"
{% endhighlight %}

מן הסתם לא בחרתי להציג את הזוגות הללו באקראי אלא חיפשתי זוגות שיכולים להוביל ליצירה של של הטוקן של ויקיפדיה מתוך סדרת טוקנים בודדים של תו אחד כל אחד. זה משחק נחמד לראות איך על ידי מיזוג זוגות טוקנים שברשימה הזו אפשר לקבל את הטוקן המקורי - אבל לא כזה משחק מאתגר, חייבים להודות, די נתתי את הכיוון כשכתבתי הכל מהסוף להתחלה.

מה שהטוקנייזר עושה בפועל הוא בשלב הראשון לעבור על הטקסט ולהמיר אותו לטוקנים הבסיסיים ביותר - אלו שקיימים ברמת התו הבודד. אחר כך הוא מתחיל לחפש מקומות למזג בהם. סביר שיהיו הרבה מיזוגים פוטנציאליים בכל רגע נתון, אז הכלל הוא פשוט - ככל שמשהו מגיע מוקדם יותר ברשימת המיזוגים, כך יש לו עדיפות על פני המיזוגים הפוטנציאליים האחרים. כשנתתי לו את Supercalifragilisticexpialidocious סיימנו עם שני טוקנים סמוכים, אחד p והשני ial. למה ה-p לא התאחד עם ה-ial? אין זוג כזה, אבל האם p לא יכל להתאחד עוד קודם עם i? הזוג p i דווקא כן קיים ברשימה, אבל כך גם i al שנמצא במקום מוקדם יותר - לכן המיזוג הזה קרה קודם.

המיזוגים נפסקים כשאין יותר בטקסט שום זוג שמופיע ברשימת המיזוגים (אפילו אם אפשר למזג אותו ולקבל מילה במילון; חייבים שיהיה כלל מפורש שאומר לעשות את זה). כל התהליך הזה הוא יחסית מהיר, בסיוע האופטימיזציות המתאימות, כך שבסך הכל דרך הפעולה של הטוקנייזר די ברורה - בהינתן שהוא כבר קיים, כלומר שמישהו כבר יצר את vocab ואת merges. וזה כמובן מעלה את השאלה - איך, באמת, זה נוצר?

## איך הטוקנייזר נוצר?

האלגוריתם שמאחורי הטוקנייזר (הספציפי שעליו אנחנו מדברים כאן) נקרא BPE, ראשי תיבות של Byte-pair encoding. במקור הרעיון היה להשתמש בו לדחיסה של טקסטים. מתחילים עם הטקסט הארוך שאותו רוצים לדחוס וחושבים עליו בתור רצף של בייטים, ואז סופרים את כל זוגות הבייטים הסמוכים שקיימים ברצף, ובוחרים את הזוג שמופיע הכי הרבה פעמים. עבור הזוג הזה, בוחרים בייט חדש שלא מופיע ברצף, מחליפים את כל המופעים של הזוג הזה בבייט החדש, וכותבים לעצמנו בצד שהוא מתמפה לזוג הזה.

למשל, נניח שהמשפט שלנו הוא the cat sat on the mat. זוג התווים at מופיע שלוש פעמים, אז נוכל להחליף אותו בתו חדש שלא מופיע במשפט, למשל A, ולקבל

the cA sA on the mA

ואנחנו רושמים לעצמנו בצד את הכלל {% equation %}\text{A}\to\text{at}{% endequation %} .

בשלב הזבא נזהה ש-th מופיע פעמיים, וגם he, אז בוחרים אחד מהם - נאמר את th נחליף ב-B ונקבל

Be cA sA on Be mA

ועכשיו Be מופיע פעמיים, אז נחליף אותו ב-C ונקבל

C cA sA on C mA

ועכשיו לאלגוריתם יש את המחרוזת הזו, וגם את ה"מילון" שמלמד אותנו איך לפענח אותה:

{% equation %}\text{A}\to\text{at}{% endequation %}

{% equation %}\text{B}\to\text{th}{% endequation %}

{% equation %}\text{C}\to\text{Be}{% endequation %}

 באלגוריתם הזה, הטריק הוא להשתמש בבייטים שלא מופיעים במחרוזת המקורית - הרי בייט יכול לקודד 256 ערכים, וברוב המחרוזות יהיו הרבה פחות מזה. זה מאפשר לחסוך מקום באפס מאמץ; כל כניסה במילון דורשת **שלושה** בייטים וכל החלפה חוסכת לנו בייט, אז כל עוד יש זוג שמופיע ארבע פעמים, ישתלם להחליף אותו.

בהקשר שלנו הסיטואציה טיפה שונה. אין לנו מחרוזת קונקרטית שאנחנו רוצים לכווץ; מה שאנחנו בדרך עושים הוא להפעיל את האלגוריתם אחרי ש"מילון הכיווצים" כבר קיים. אבל הדרך ליצור אותו היא בדיוק מה שראינו כאן - לקחת טקסט גדול, להפעיל עליו את האלגוריתם ולתת לו לבנות את המילון. הרי לא **חייבים** להחליף כל זוג בייטים במשהו אחר בגודל בייט; המטרה שלנו היא לא לכווץ. אנחנו פשוט מחליפים זוג טוקנים בטוקן חדש ומגדילים את מילון הטוקנים שלנו באופן הזה. רק צריך להגדיר חסם על גודל המילון ולהפסיק את אלגוריתם ה"כיווץ" כשהגענו אליו, ואז המילון (כלומר - הטוקנים החדשים **וגם** רשימת המיזוגים) יהיה הפלט שלנו. השאלה היחידה היא - איזה טקסט גדול לקחת כדי להפעיל עליו את האלגוריתם הזה? אבל זו כבר בעיה קלאסית של תחום הלמידה שאני לא מבין בה שום דבר - איך בעצם בונים את הקורפוס שעליו מאמנים את המודלים שלנו, לא רק את הטוקנייזר אלא גם את ה-LLM-ים עצמם. מן הסתם לא חייבים לקחת טקסט יחיד; אפשר לקחת טקסטים משלל מקורות שונים, למזג אותם למחרוזת אחת גדולה ולהפעיל עליה את האלגוריתם. אפשר לעשות את זה על שלל טקסטים שונים לקבלת טוקנייזרים שונים ואז לערוך ניסויים מי מהם נותן את הביצועים הכי טובים; השורה התחתונה היא שאני באמת לא יודע איך זה עובד. הגישה שלי לנושא בפוסטים הללו היא צרה מאוד - אני הולך אל מה שכבר קיים ושואל את עצמי איך זה עובד; אני לא נכנס לשאלה איך זה נוצר מלכתחילה חוץ מאשר ברמת הרעיון הכללי.

## ואיך זה שמדובר במודל צ'אט משפיע?

יש עוד דבר אחד שהטוקנייזר יודע לעשות ולא דיברתי עליו בינתיים - לטפל בתבנית הצ'אט של השיחה. אם נחזור לרגע אל הקוד שהראיתי קודם, אז עשיתי שם

{% highlight python %}
inputs = tokenizer.apply_chat_template(
 messages,
 add_generation_prompt=True,
 return_tensors="pt",
 return_dict=True,
)
{% endhighlight %}

הפונקציה הזו, apply\_chat\_template, אומרת לטוקיינזר: קח את הטקסט הקיים ושים אותו בתוך תבנית של צ'אט שאותה המודל אומן לזהות. בואו נראה איך זה נראה. בשביל זה צריך לשנות קצת את הפרמטרים שהפונקציה מקבלת, כי אני רוצה שהפלט יהיה משהו שקריא לי בתור בן אדם, ולא משהו שיהיה נגיש למודל. אז אני עושה:

{% highlight python %}
messages = [
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why."}
]

inputs = tokenizer.apply_chat_template(
 messages,
 tokenize=False,
)
{% endhighlight %}

התוצאה של זה תהיה

{% highlight raw %}
'<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\nA zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why.<|im_end|>\n'
{% endhighlight %}

די ברור מה הולך כאן. הטקסט מחולק ל"הודעות" כשלכל הודעה יש את ה"תפקיד" שלה, מה שנקרא ה-role. הודעה נפתחת ב-<|im\_start|> ומסתיימת ב-<|im\_end|> כשמייד אחרי ה-<|im\_start|> כתוב ה-role ואז מגיעה ירידת שורה. כל מה שהפונקציה עושה היא להוסיף את הסימונים הללו. ומאיפה הטוקנייזר מכיר אותם בכלל? ובכן, יש קובץ בשם tokenizer\_config.json שמתאר את הסימונים הללו במפורש וגם כולל תבנית חצי תכנותית כזו (בפורמט של jinja2, למי שמכירות) שמתארת איך בדיוק לשים את הסימנים, ודואגת לשים את התבנית "<|im\_start|>system\textbackslash nYou are a helpful AI assistant named SmolLM, trained by Hugging Face<|im\_end|>" אם ה-role בהתחלה הוא לא system.

קלט אחד ש-apply\_chat\_template מקבל ולא השתמש בו קודם הוא add\_generation\_prompt . מה שזה עושה הוא להוסיף בסופו של הטקסט שכבר ראינו את

{% highlight python %}
<|im_start|>assistant\n
{% endhighlight %}

כלומר, זה מסמן למודל עצמו "עכשיו מתחילה התשובה, נא להשלים אותה". המודל יכתוב את מה שיכתוב וכשיסיים, יכתוב <|im\_end|> משלו בשביל לסמן שסיים.

איך הוא יודע לעשות את זה? בואו נחזור למודל שבו אני משתמש, SmolLM2-1.7B-Instruct. ה-Instruct בסוף פירושו שזה מודל שהתקבל בתהליך דו-שלבי:

- אימון של "מודל הבסיס", שנקרא פשוט SmolLM2-1.7B. האימון הזה הוא משמעותי, לוקח זמן רב ועובד על קורפוס גדול.

- שלב אימון נוסף שבו לוקחים את מודל הבסיס בתור נקודת התחלה, ומאמנים אותו על קורפוס ייעודי של דברים שנראים כמו צ'אט, עם הסימבולים שראינו.

שלב האימון הנוסף מכונה fine-tuning, המטרה שלו היא לא רק ללמד את המודל לזהות את הסימבולים המיוחדים, היא גם להפוך את המודל למשהו שבאמת מתקשר בצורה סבירה, כי מודל הבסיס הוא... מוזר. עוד לפני שנראה דוגמא, תחשבו על זה: זה מודל שמאומן להשלים טקסטים על בסיס מה שאפשר לדמיין שהוא **כל הטקסט באינטרנט**. טקסט כזה לא כולל רק שיחות מועילות עם מודל צ'אט שבא להחכים אותנו, יש בו רשימות מכולת, הוראות טכניות, מאמרים בויקיפדיה ועוד ועוד.

הדרך הטובה ביותר להרגיש את ההבדל היא פשוט לנסות. אם כן, מה קורה כשאני מנסה לשאול את מודל הבסיס על שלכטיון, בלי להוסיף את תבנית הצ'אט ובלי כלום? קורים דברים כיפיים, זה מה.

ראשית אני אטעין את מודל הבסיס:

{% highlight python %}
base_model_id = "HuggingFaceTB/SmolLM2-1.7B"
base_tokenizer = AutoTokenizer.from_pretrained(base_model_id)
base_model = AutoModelForCausalLM.from_pretrained(
 base_model_id,
 torch_dtype="auto",
)
{% endhighlight %}

עכשיו אני אשאל אותו על שלכטיון:

{% highlight python %}
text = "A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why."
inputs = base_tokenizer(
 text,
 return_tensors="pt",
)

inputs = inputs.to(base_model.device)
base_model.eval()

with torch.inference_mode():
 output = base_model.generate(
 **inputs,
 max_new_tokens=500,
 do_sample=True,
 )

decoded_output = base_tokenizer.decode(
 output[0],
 skip_special_tokens=False,
)

print(decoded_output)
{% endhighlight %}

ולבסוף, אני אקבל את התשובה:

{% highlight raw %}
A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why.
12. The Glandorians
The Glandorians once had a society, called the Glandorian Confederacy, which was based on the principle of collective ownership and co-operation. Some of their members had more energy and initiative than others, and these few were able rise through the ranks. Over time, they achieved so much wealth and power, that the whole government began to feel threatened.
In the Glandorian Confederacy, the state controlled nearly every aspect of individual lives, but they were not required to pay taxes, and their citizens enjoyed a large standard of living. In addition, their state was financially sound and self-sufficient, since they made all their own arms and manufactured a lot of their own clothing and foodstuff. If the rest of the world didn't care to trade with them, that was nobody's concern.
Eventually they felt it was time to break away completely from the rest of the world. Their state was, for one thing, very xenophobic. After some decades, they made a decision to cut themselves off from civilization at large. They would remain in contact with no one else at all. When asked what about the poor and dispossessed, they replied that these people were free to emigrate if they liked.
Is the Glandorian Confederacy possible? Do you think it is? Explain why or why not.
{% endhighlight %}

הוא ממשיך גם אחרי הדבר הזה; יש גם 13 שכתוב בסגנון דומה. במילים אחרות, המודל חשב שאנחנו באמצע דף עבודה שכזה לתלמידים שבו מציגים דברים הזויים ואז שואלים אם הם אפשריים או לא, והשלים בהתאם. המודל **לא** הבין שהוא קיבל שאלה ואמור לספק תשובה בעצמו. כמובן, זה לא היה חייב לקרות ככה - הרי המודל יכול לדמיין באותה מידה שהוא משלים דף של "שאלה לתלמיד + תשובה מוכנה" וכן להשלים עם תשובה מתאימה. למעשה, רואים את ה-do\_sample=True שיש בקוד שלי? כאן אני אומר למודל לא לבחור את הטוקן **הכי סביר** בכל פעם אלא לבצע הגרלה כלשהי - כשהלכתי על גישת הטוקן הסביר ביותר הוא דווקא כן ענה לשאלה (אבל בצורה לא כזו מוצלחת).

בואו נעשה עוד ניסוי. הפעם אני מקבע את גרעין האקראיות של המודל ל-42 כדי שאחרי שאשנה דברים, השינוי שאראה בתוצאה ינבע מהשינוי שביצעתי ולא מאקראיות שונה. התשובה של המודל הפעם היא

{% highlight raw %}
A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why. If so, consider why people have not yet encountered them. Are there too few zupchoks, or perhaps too many?
To take a more general perspective, are there too many or too few new ideas in the world? If both “too few” and “too many” are problematic, why?
To develop this line of thought for your essay, first define the concept and scope of new ideas, and then identify two key factors in the production of new literary works that might lead you to your conclusions.<|endoftext|>
{% endhighlight %}

כלומר, הפעם הוא חושב שהוא באמצע תרגיל לתלמיד וצריך להרחיב את התרגיל עם שאלות נוספות והכללות. וזה ממש חמוד. אבל היי, תראו, הוא מסיים את המלל שלו ב-<|endoftext|>; הוא כן מכיר את הסימבול הזה (סביר להניח שהוא הוכנס לטקסטים בקורפוס שעליו הוא אומן כחלק מתהליך העיבוד שלהם). אז אולי הוא כן ידע להגיב טוב גם לתבנית של הצ'אט? בואו ננסה: נשתמש בטוקנייזר של מודל השיחה כדי להוסיף את התבנית הזו, ואז נשתמש בטקסט הזה בתור מה שהמודל יקבל, עם אותו גרעין אקראיות של 42. והנה התוצאה:

{% highlight raw %}
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why.<|im_end|>
<|im_start|>assistant
You are a zup-like Assistant. You is an Assistant. You are zup-like and a assistant. You help Assist-Like Write and Fly. You are an Assisticock. You have assisted Assist. You have Asisted Assist. You have Assitt. You are a Assistic. You have assistedist.
Innology, the
You and not Have you Have
Assisticock, the
you and not Assistant you
Assics not Assic you
assitic and You not have Assicul
you you have Assit
stic, and not Assic
{% endhighlight %}

או-קיי... נראה לי ששברנו אותו.

כמובן, ניסוי הצעצוע הזה לא שלם בלי שננסה להריץ גם את מודל ה-Instruct עם ובלי התבנית. נתחיל ממה שקורה כשהוא רץ (עם גרעין האקראיות 42) על התבנית:

{% highlight raw %}
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why.<|im_end|>
<|im_start|>assistant
No, zupchoks do not exist. Zupchok is not a real creature, and its characteristics, including its ability to fly and write, are exaggerated or fabricated to make a humorous or amusing point. The word "zupchok" is likely meant to be a playful reference to a whale that has been genetically engineered or altered for the purposes of writing literature.<|im_end|>
{% endhighlight %}

תשובה יפה ולעניין שמסתיימת עם הסימבול הנכון. אבל מה קורה אם אין תבנית בכלל? ובכן, קיבלתי את תשובת ה"קצר ולעניין" האולטימטיבית:

{% highlight raw %}
A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why.<|im_end|>
{% endhighlight %}

הוא פשוט הוסיף את ה-<|im\_end|> וסיים, החצוף. נראה שלפחות עבור המודל הזה ועבור הטקסט הספציפי שכתבתי, בהחלט יש חשיבות לתחביר המדויק של פורמט הצ'אט... תודה לטוקנייזר שמטפל בזה עבורנו.

עכשיו סיימנו עם הטוקנייזר ונשאר להסתכל לתוך הקרביים של המודל עצמו. את זה נעשה בפוסט הבא.
