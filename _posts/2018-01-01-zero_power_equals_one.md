---
id: 3528
title: "אז למה דברים בחזקת 0 שווים 1?"
date: 2018-01-01 13:50:48
layout: post
categories: 
  - מספרים
tags: 
  - אלגברה בסיסית
  - חזקת אפס
  - מבוא למתמטיקה
---
שאלה שאני נתקל בה לא מעט ולא נראה לי שאי פעם עניתי עליה בבלוג היא למה להעלות דברים בחזקת 0 יוצא 1. זה אחד מאותם דברים שנלמדים בבית הספר ויכולים להרגיש שרירותיים מאוד אבל אפשר לתת להם הצדקה אינטואיטיבית בקלות רבה יחסית, ולומר עליהם עוד דברים מעניינים בנוסף.

אז הנה הצדקה אינטואיטיבית. מה זו בכלל "העלאה בחזקה"? כשאני כותב {% equation %}x^{2}{% endequation %} זו דרך מקוצרת לתאר <strong>כפל</strong>: {% equation %}x^{2}=x\times x{% endequation %}. באופן דומה עושים את זה עם חזקות גדולות יותר:

{% equation %}x^{3}=x\times x\times x{% endequation %}

{% equation %}x^{4}=x\times x\times x\times x{% endequation %}

וכן הלאה. נקודת ה"התחלה" שאנחנו רגילים אליה היא {% equation %}x^{1}=x{% endequation %}, וכדי להתקדם קדימה מנקודת ההתחלה הזו אנחנו פשוט כופלים שוב ושוב ב-{% equation %}x{% endequation %}: אם אני לוקח את {% equation %}x^{2}{% endequation %} וכופל אותו ב-{% equation %}x{% endequation %} אני אקבל את {% equation %}x^{3}{% endequation %} וכן הלאה.

<strong>באותו אופן בדיוק</strong> אפשר ללכת אחורה על ידי <strong>חלוקה</strong> ב-{% equation %}x{% endequation %}: אם אני לוקח את {% equation %}x^{3}{% endequation %} ומחלק אותו פעם אחת ב-{% equation %}x{% endequation %} אני אקבל את {% equation %}x^{2}{% endequation %} כי אחד מה-{% equation %}x{% endequation %}-ים בכפל "מתבטל". באופן דומה, אם אקח את {% equation %}x^{2}{% endequation %} ואחלק אותו ב-{% equation %}x{% endequation %} נקבל {% equation %}x{% endequation %}. עכשיו, אם אני לוקח את {% equation %}x^{1}{% endequation %} ומחלק אותו ב-{% equation %}x{% endequation %}, מה אני אקבל? כל חלוקה ב-{% equation %}x{% endequation %} מקטינה את החזקה ב-1, אז מה שאני אמור לקבל הוא {% equation %}x^{0}{% endequation %}; ומצד שני, על פי ההגדרה היבשה, לקחת את {% equation %}x^{1}{% endequation %} ששווה ל-{% equation %}x{% endequation %} ולחלק אותו ב-{% equation %}x{% endequation %} זה אומר לקבל את {% equation %}\frac{x}{x}=1{% endequation %} - כי כל מספר שמחלקים אותו בעצמו יוצא 1. חוץ מאשר {% equation %}x=0{% endequation %}. אפס הוא מקרה מיוחד ומסובך יותר. נדבר עליו בהמשך.
<h2>חוקי חשבון</h2>
הנה דרך מסודרת יותר לדבר על הרעיון הזה - <strong>חוקי החשבון של חזקות</strong>. בבית הספר לומדים את הכלל הבא: {% equation %}x^{a}\times x^{b}=x^{a+b}{% endequation %}. הכלל הזה נכון כאשר {% equation %}a,b{% endequation %} הם מספרים שלמים חיוביים, למשל {% equation %}2^{2}\times2^{3}=2^{5}{% endequation %}. למה זה עובד? כי {% equation %}2^{2}{% endequation %} זה בסך הכל לכתוב {% equation %}2\times2{% endequation %} ולכתוב {% equation %}2^{3}{% endequation %} זה בסך הכל לכתוב {% equation %}2\times2\times2{% endequation %}. אז לכתוב {% equation %}2^{2}\times2^{3}{% endequation %} זה כמו לכתוב {% equation %}\left(2\times2\right)\times\left(2\times2\times2\right){% endequation %}. אם נספור כמה פעמים 2 מופיע במכפלה הזו נקבל את סכום הפעמים שהוא מופיע בסוגריים הימניים ובסוגריים השמאליים.

ברגע שבו יש לנו פעולת חיבור, אוטומטית אפשר לדבר גם על חיסור. אם {% equation %}a+b=c{% endequation %} עבור שלמים חיוביים {% equation %}a,b,c{% endequation %}, אז {% equation %}a=c-b{% endequation %} - זו המהות של פעולת החיסור. אפשר לקחת את זה גם לפעולת החזקה כדי להגדיר את המשמעות של <strong>חיסור חזקות</strong>: אם {% equation %}x^{c}=x^{a+b}=x^{a}\times x^{b}{% endequation %} אז מצד אחד {% equation %}x^{a}=\frac{x^{c}}{x^{b}}{% endequation %} (כי נחלק את שני האגפים של {% equation %}x^{c}=x^{a}\times x^{b}{% endequation %} ב-{% equation %}x^{a}{% endequation %}) ומצד שני {% equation %}x^{a}=x^{c-b}{% endequation %} (כי כבר אמרנו ש-{% equation %}a=c-b{% endequation %}). כלומר, מכלל ה<strong>חיבור</strong> של חזקות קיבלנו את השוויון הבא: {% equation %}x^{c-b}=\frac{x^{c}}{x^{b}}{% endequation %}. חיסור של חזקות מתפרש אצלנו בתור <strong>חלוקה</strong>. אם מקבלים את הגישה הזו, אז זה ש-{% equation %}x^{0}{% endequation %} הוא 1 זה מתבקש: {% equation %}x^{0}=x^{a-a}=\frac{x^{a}}{x^{a}}=1{% endequation %} לכל {% equation %}a{% endequation %} שלם חיובי.

מה שנחמד בגישה הזו של המינוס היא שהיא גם מציעה לנו מייד דרך להגדיר חזקות <strong>שליליות</strong>: למשל, {% equation %}x^{-1}=x^{0-1}=\frac{1}{x}{% endequation %}, ובאופן כללי מקבלים {% equation %}x^{-a}=\frac{1}{x^{a}}{% endequation %}. הדרך הזו עקבית עם המחשבה על חיסור בתור "חיבור עם מינוס של מספר", כי

{% equation %}x^{a-b}=x^{a+\left(-b\right)}=x^{a}\times x^{-b}=x^{a}\times\frac{1}{x^{b}}=\frac{x^{a}}{x^{b}}{% endequation %}

אגב, הגישה הזו היא גם מה שמוביל להגדרה של דברים כמו {% equation %}x^{\frac{1}{2}}=\sqrt{x}{% endequation %} וכדומה. יש כלל חזקות נוסף שמדבר על <strong>מכפלה</strong> של חזקות: {% equation %}x^{a\times b}=\left(x^{a}\right)^{b}{% endequation %}, אז אפשר להשתמש בו כדי להשתכנע שיהיה נוח להגדיר את {% equation %}x^{\frac{1}{2}}{% endequation %} בתור משהו שמקיים {% equation %}\left(x^{\frac{1}{2}}\right)^{2}=x^{\frac{1}{2}\times2}=x^{1}=x{% endequation %}, כלומר ש-{% equation %}x^{\frac{1}{2}}{% endequation %} יהיה שורש של {% equation %}x{% endequation %}. אני כן חייב להעיר שהסיפור די מסתבך כאן כי ל-{% equation %}x{% endequation %} יכול להיות <strong>יותר משורש אחד</strong>, ולכן כשמגדירים את {% equation %}x^{\frac{1}{2}}{% endequation %} בוחרים את אחד מהשורשים האפשריים בצורה קצת שרירותית.
<h2>הגדרה רקורסיבית</h2>
אני רוצה להציג עכשיו את מה שכבר הסברתי, אבל בלבוש טיפה שונה, שאני מקווה שיהיה מעניין למי שלא מכיר אותו עדיין - <strong>הגדרה רקורסיבית</strong> של פעולת החזקה. להגדיר משהו באופן רקורסיבי פירושו להגדיר אותו "בעזרת עצמו על מקרה יותר פשוט". הגדרה רקורסיבית כוללת בדרך כלל שני מרכיבים: הגדרה למקרה "הכי פשוט" שהיא ישירה, והגדרה "עקיפה" למקרים יותר מסובכים. הנה הגדרה עקיפה שכזו של חזקה:

{% equation %}x^{n+1}=x^{n}\times x{% endequation %}

מה הולך פה? ההגדרה אומרת את הדבר הבא: <strong>נניח</strong> שאנחנו כבר יודעים להגדיר את החזקה ה-{% equation %}n{% endequation %}-ית של {% equation %}x{% endequation %}. עכשיו אפשר להגדיר את החזקה {% equation %}x^{n+1}{% endequation %} בעזרתה: נגדיר אותה בתור המכפלה של {% equation %}x{% endequation %} ב-{% equation %}x^{n}{% endequation %}.

על פניו, מה ההבדל הגדול בין לומר את זה ובין לומר שנגדיר את {% equation %}x^{n}{% endequation %} להיות {% equation %}x\times x\times\dots\times x{% endequation %} במשך {% equation %}n{% endequation %} פעמים? לא נראה שיש הבדל גדול, אבל שימו לב שכן יש הבדלים. בניסוח ה"ישיר" אני משתמש בכל מני סימנים שהם קצת מעורפלים מבחינה מתמטית: השלוש נקודות הללו שבאות באמצע הכפל, וה"במשך {% equation %}n{% endequation %} פעמים" שהוא ביטוי מילולי. אני לא אומר שזו לא הגדרה פורמלית לגמרי, כי היא כן; אבל הפורמליזם שלה מסתמך על כך שאתם, הקוראים, יודעים להשלים פרטים בראש. למחשב יהיה יותר קשה להתמודד עם הגדרה כזו. בשל כך, הגדרות רקורסיביות שכאלו הן משהו ידידותי יותר למחשבים, ומועילות יותר בהקשר הזה.

עדיין, ההגדרה שנתתי למעלה היא בעייתית כי אין לה <strong>תנאי עצירה</strong> - אין לה מקרה פשוט כל כך שבו אפשר לעצור ולהחזיר תשובה ישירה. אפשר היה לעשות את תנאי העצירה ב-{% equation %}n=1{% endequation %}, שיהיה {% equation %}x^{1}=x{% endequation %} וחסל; אבל אפשר באותה המידה גם להגדיר תנאי עצירה ב-{% equation %}n=0{% endequation %}. נניח שאנחנו לא יודעים ש-{% equation %}x^{0}=1{% endequation %}; איך נכון לנו להגדיר באופן ישיר את {% equation %}x^{0}{% endequation %}?

ובכן, אנחנו רוצים שיתקיים {% equation %}x^{1}=x^{0+1}=x^{0}\times x{% endequation %}. הדרך היחידה שבה {% equation %}x^{1}=x^{0}\times x{% endequation %} תתקיים היא אם {% equation %}x^{0}=1{% endequation %}, ולכן גם ההגדרה הרקורסיבית מזמינה את ההגדרה {% equation %}x^{0}=1{% endequation %}, הפעם בתור מקרה הבסיס שלה.
<h2>"מכפלה ריקה"</h2>
ועכשיו, הנה דרך <strong>שונה</strong> לחשוב על הסיפור הזה. לאו דווקא טובה או גרועה יותר, אבל שונה. בואו נשחק משחק - וחשוב שנשחק אותו כדי להפעיל את האינטואיציה כאן: מה סכום כל המספרים הקטנים או שווים ל-100 שמתחלקים גם ב-5 וגם ב-7?

ובכן, יש בדיוק שני מספרים כאלו: 35 ו-70, ולכן הסכום שלהם הוא 105. אם אתם רוצים נימוק (וזה ממש לא חשוב כאן), זה נובע מכך ש-5 ו-7 שניהם <strong>ראשוניים</strong> ולכן מספר שמתחלק על ידי שניהם בפרט מתחלק על ידי המכפלה שלהם, שהיא 35.

עכשיו בואו נשאל את אותה שאלה עם פרמטרים שונים: מה סכום כל המספרים הקטנים או שווים ל-100 שמתחלקים גם ב-11 וגם ב-13?

כמקודם, שני אלו מספרים ראשוניים ולכן המספר הקטן ביותר שמתחלק בשניהם הוא המכפלה שלהם, 143. והמספר הזה גדול מ-100, כלומר בכלל <strong>לא קיימים</strong> מספרים קטנים או שווים ל-100 שמתחלקים גם ב-11 וגם ב-13. אז מה הסכום הולך לצאת?

חלקכם יענו "אפס" בשלב הזה, וזה מה שאני מכוון אליו; אבל חלקכם יענו "לא מוגדר", ואתם צודקים באותה מידה. לא לגמרי ברור אם <strong>אמור</strong> להיות סכום לקבוצה ריקה של מספרים. אבל אני רוצה לתת אינטואיציה לכך ש<strong>כדאי</strong> שיהיה לה סכום. נניח שאני כותב תוכנית מחשב שמסיבות אלו ואחרות, עבור הרבה זוגות של ראשוניים מחשבת את הסכום של המספרים עד 100 שמתחלקים בזוגות הללו. אז אני אכתוב קטע קוד שמקבל שני מספרים ראשוניים ומחזיר את הסכום של כל המספרים עד 100 שמתחלקים בהם, ואז אני אפעיל את קטע הקוד הזה כמה פעמים שונות ואחבר את התוצאות של כל הפעמים הללו. פעם אחת אפעיל עם 5 ו-7 ואקבל 105, ובפעם אחרת אפעיל עם 11 ו-13 ואקבל... ובכן, לא הייתי רוצה שההפעלה על 11 ו-13 "תקלקל" לי את המשך החישוב, ואם בהפעלה הזו אני אקבל חזרה "תוצאה לא מוגדרת" ואנסה לחבר אותה עם 105 לא יצא לי שום דבר מועיל.

מה שאני רוצה הוא פשוט <strong>להתעלם</strong> מההפעלה על 11 ו-13. לכן אני רוצה שהיא תחזיר מספר שחיבור בו הוא התעלמות ממנו. המספר הזה הוא רק 0: אפס שמחובר עם כל {% equation %}x{% endequation %} מחזיר את {% equation %}x{% endequation %}, כאילו 0 בכלל לא השתתף במשחק. זאת להבדיל מחיבור "משהו לא מוגדר" עם {% equation %}x{% endequation %} שיחזיר "משהו לא מוגדר" או יגרום לתוכנה שלנו לקרוס.

החשיבות של אפס כאן היא בהיותו <strong>אדיש ביחס לפעולת החיבור</strong>. אבל מה קורה עם פעולת <strong>כפל</strong>? אם אני כופל את {% equation %}x{% endequation %} ב-0 אני אקבל 0; כלומר, כפל באפס לא "מתעלם" מהאפס, אלא ההפך - יש לו אפקט "הרסני", שתלטני. הוא מוחק את ה-{% equation %}x{% endequation %} לגמרי. אז למרות ש-0 הוא סביר בהחלט בתור <strong>סכום</strong> של קבוצה ריקה של איברים, הוא ממש לא סביר בתור <strong>מכפלה</strong> של קבוצה ריקה של איברים. כאן האינטואיציה היומיומית שלנו כנראה נגמרת.

אז מה כדאי לנו לבחור בתור המכפלה של קבוצה ריקה של איברים? עבור סכום רצינו את האיבר האדיש ביחס לחיבור, כלומר 0; אז עבור מכפלה נרצה את האיבר האדיש ביחס לכפל, כלומר 1.

ואיך זה מתקשר לחזקה? ובכן, אם {% equation %}x^{n}{% endequation %} זו מכפלה של {% equation %}x{% endequation %} בעצמו בדיוק {% equation %}n{% endequation %} פעמים, אפשר לחשוב על זה כאילו אנחנו לוקחים סדרה שמכילה בדיוק {% equation %}n{% endequation %} עותקים של {% equation %}x{% endequation %} וכופלים את כל האיברים בה. ואם {% equation %}n=0{% endequation %}, זו תהיה קבוצה ריקה של מספרים, שלא מכילה אפילו עותק בודד של {% equation %}x{% endequation %}, ולכן המכפלה הזו היא "המכפלה הריקה" במקרה הזה, ושווה ל-1.
<h2>כמה מחרוזות יש?</h2>
והנה עוד גישה שונה לגמרי לכל הסיפור הזה, שייתכן ותיראה מאוד מוזרה במבט ראשון, אבל לדעתי היא פותחת עיניים. היתרון הגדול ביותר שלה הוא בכך שהיא תיתן לנו אינטואיציה כלשהי לגבי מה אמור לקרות עם החזקה המושמצת ביקום: {% equation %}0^{0}{% endequation %}, שעדיין לא התייחסתי אליה ישירות.

הנה שאלה: כמה מילים מאורך 2 אפשר להרכיב מהאותיות א', ב', ג'? התשובה שלי היא ש-9 מילים:

"אא", "אב", "אג", "בא", "בב", "בג", "גא", "גב", "גג".

אתם עשויים להסכים איתי, או שתציינו, ובצדק רב, שרוב מה שכתבתי פה הוא לא מילים. האם "אא" זו מילה חוקית בשפה העברית? בוודאי שלא. לכן אני אחדד את הניסוח שלי: אני לא שואל כמה <strong>מילים</strong> אפשר להרכיב, אלא כמה <strong>מחרוזות</strong> אפשר להרכיב. "מחרוזת" היא סדרה של אותיות (ב"סדרה" אני מתכוון שהסדר חשוב - "אב" ו"בא" הן שתי מחרוזות שונות) בלי שתהיה דרישה שהסדרה הזו תיתן משהו שאפשר להגות אותו בצורה נורמלית, או שישתמשו בו בפועל בשפה כלשהי, וכדומה. תחשבו על <strong>ססמאות</strong> - על פי רוב כשאנחנו כותבים ססמאות אנחנו כותבים מחרוזות שאנחנו דווקא <strong>לא רוצים</strong> שיהיו מילים חוקיות בפני עצמן (הסתייגות אחת - ססמא שהיא צירוף של כמה מילים לא קשורות יכולה להיות בסדר גמור). בקיצור, מחרוזות זה עניין שימושי ונפוץ במדעי המחשב, אז בואו נדבר עליהן בתור הדוגמא שלנו.

עכשיו, בואו נבין איך הגענו לבדיוק 9 מחרוזות שהן מאורך 2 ועם אותיות מתוך א',ב',ג': יש לנו 3 אפשרויות לבחירה של האות הראשונה במחרוזת, ו-3 אפשרויות לבחירה של האות השניה במחרוזת, ושתי האפשרויות הללו בלתי תלויות זו בזו (זה לא שאם בחרתי א' בתור אות ראשונה אז אסור לי לבחור אותה בתור אות שניה, למשל). אז עבור כל אחת מ-3 הבחירות האפשריות לאות ראשונה יש לי 3 אפשרויות שונות לאות שניה, ולכן בסך הכל {% equation %}3\times3=9{% endequation %}.

באופן דומה אם הייתי צריך לבנות מילים מאורך 3, אז היו לי {% equation %}3\times3\times3=27{% endequation %} אפשרויות. ועבור מילים באורך {% equation %}4{% endequation %} הייתי מקבל {% equation %}3\times3\times3\times3=81{% endequation %} וכן הלאה. באופן כללי, עבור מחרוזת מאורך {% equation %}n{% endequation %} הייתי מקבל {% equation %}3^{n}{% endequation %} אפשרויות. ועכשיו נשאלת השאלה - מה עם מחרוזת מאורך 0?

כמקודם, יש לנו שתי אפשרויות. לומר "אין דבר כזה מחרוזת מאורך 0", או לזרום עם זה שכדאי שתהיה כזו מחרוזת ולנסות לענות על השאלה. אני אישית בעד גישת "יש מחרוזת מאורך 0". ראשית כי קל לי לכתוב כזו: אם כתבתי קודם "אב" בתור מחרוזת לדוגמא מאורך 2, אז מחרוזת מאורך 0 היא פשוט "" - זוג המרכאות שמציין את תחילת וסוף המחרוזת, בלי שום תוכן באמצע. נראה לכם מטופש? זה מה שעושים בפועל כשמתכנתים.

פרט לכך, למה שלא תהיה מחרוזת מאורך 0? הרבה פעמים אנחנו ממלאים טפסים ממוחשבים ומשאירים שדה זה או אחר ריק (למשל, את שדה "הערות נוספות"). אפשר לחשוב על זה בתור "אין מחרוזת" אבל אפשר גם באותה מידה לחשוב על זה בתור "מחרוזת מאורך 0", ובדבר השני קל יותר לטפל עם קוד כללי.

אם כן, הסכמנו ש<strong>יש</strong> מחרוזת מאורך 0. האם יש <strong>יותר ממחרוזת אחת</strong> מהאורך הזה? לא. כי מחרוזות הן שונות זו מזו אם אני יכול להגיד "במקום כך-וכך מופיעה במחרוזת הראשונה אות מסויימת ובמחרוזת השניה באותו מקום מופיעה אות אחרת". כלומר, כדי להבדיל בין שתי מחרוזות שונות אני צריך בפרט שיהיו בהן אותיות. זה לא קיים במחרוזת מאורך 0, ולכן יש בדיוק אחת כזו. על כן, אם {% equation %}3^{n}{% endequation %} מייצג את מספר המחרוזות מאורך 0 שבנויות משלוש אותיות אפשריות, אז {% equation %}3^{0}=1{% endequation %} צץ מאליו.

כמובן, המספר 3 פה הוא לא מיוחד. אם הייתי מדבר על מחרוזות שבנויות על ארבע האותיות א', ב', ג', ד', אז היו לי {% equation %}4^{n}{% endequation %} מחרוזות מאורך {% equation %}n{% endequation %} - ושוב, עבור {% equation %}n=0{% endequation %} הייתי מקבל 1. באופן כללי אם יש לי {% equation %}k{% endequation %} אותיות אז יש {% equation %}k^{n}{% endequation %} מחרוזות מאורך {% equation %}n{% endequation %} שאפשר לכתוב באמצעות האותיות הללו.

ומה אם {% equation %}k=0{% endequation %}? מה אם אין לי אותיות בכלל?

ובכן, אם אין אותיות בכלל, אז אי אפשר לכתוב מחרוזת מאורך 1, כי "אורך 1" זו דרך להגיד "מופיעה בדיוק אות אחת". גם מאורך 2 אין מחרוזות. גם מאורך 5, וכן הלאה. באופן כללי יש {% equation %}0^{n}=0{% endequation %} מחרוזות מאורך {% equation %}n{% endequation %} לכל {% equation %}n{% endequation %} חיובי. אבל מה אם {% equation %}n=0{% endequation %}? במקרה הזה, המחרוזת "", זו שאינה כוללת אותיות כלל, <strong>היא עדיין מחרוזת חוקית</strong>! כלומר, למרות שמאורך חיובי יש לנו 0 מחרוזות, דווקא מהאורך הקטן יותר 0 יש לנו מחרוזת אחת. זה אומר שאם <strong>עבור המקרה הזה</strong> אני אבחר להגדיר {% equation %}0^{0}=1{% endequation %}, הנוסחה {% equation %}k^{n}{% endequation %} שמצאתי קודם למספר המחרוזות מאורך {% equation %}n{% endequation %} שאפשר לכתוב באמצעות {% equation %}k{% endequation %} אותיות - הנוסחה הזו תעבוד באופן מושלם גם עבור {% equation %}k=0{% endequation %}.
<h2>מה קורה עם אפס?</h2>
אחרי שאולי שכנעתי אתכם לפני רגע שכדאי להגדיר {% equation %}0^{0}=1{% endequation %}, בואו נדבר קצת יותר על מה הקשר של אפס לכל הסיפור הזה. קודם כבר הזכרתי את התכונה ה"שתלטנית" של אפס: {% equation %}x\times0=0{% endequation %} תמיד. לכל {% equation %}x{% endequation %}. למי שסקפטי, הנה הוכחה זריזה: {% equation %}x\times0=x\times\left(0+0\right)=x\times0+x\times0{% endequation %} ועכשיו תעבירו אגפים.

ה"שתלטנות" הזו של אפס גורמת לכך שלא תהיה לנו דרך ברורה לחלק בו תוך שמירה על חוקי החשבון הרגילים. כי אם {% equation %}\frac{x}{0}=y{% endequation %} זה אומר ש-{% equation %}x=0\times y{% endequation %}, אז {% equation %}0\times y=0{% endequation %}. במילים אחרות, אם {% equation %}x{% endequation %} לחלק ב-0 היה יוצא מספר כלשהו והיינו רוצים לשמור את החוק הזה ש-{% equation %}\frac{x}{0}=y{% endequation %}, אז היה נובע מכך שבהכרח ש-{% equation %}x{% endequation %} עצמו הוא 0. אבל גם במקרה הזה, לא לגמרי ברור איך נכון להגדיר את {% equation %}\frac{0}{0}{% endequation %}; אם אני אגדיר {% equation %}\frac{0}{0}=0{% endequation %} אז זה יצא "הגיוני" במובן זה ש-{% equation %}0=0\times0{% endequation %}, אבל גם אם אגדיר {% equation %}\frac{0}{0}=1{% endequation %} זה יצא "הגיוני" במובן זה ש-{% equation %}0=0\times1{% endequation %}. במילים אחרות, אין לנו הגדרה טובה גם ל-{% equation %}\frac{0}{0}{% endequation %}. זה מה שנקרא "ביטוי לא מוגדר" אצלנו, ומסיבה טובה.

מכיוון שאי אפשר לחלק ב-0, האינטואיציה שהשתמשנו בה קודם, של לומר {% equation %}0^{a-b}=\frac{0^{a}}{0^{b}}{% endequation %}, פשוט לא עובדת. הביטוי באגף ימין לא מוגדר. זו סיבה טובה מאוד לומר ש-{% equation %}0^{0}{% endequation %} הוא ביטוי לא מוגדר. בוודאי ובוודאי שביטוי כמו {% equation %}0^{-1}=\frac{1}{0}{% endequation %} יהיה בלתי מוגדר; אנחנו אפילו לא מנסים לדבר על חזקות שליליות של 0. אבל הדיון על {% equation %}0^{0}{% endequation %} עצמו לא נגמר פה.

למה שלא ייגמר? כי ראינו שיש בעיה בשימוש בנימוק הראשון שלי, זה של חוקי החשבון של חזקות, אבל כל הנימוקים האחרים שהבאתי - רקורסיה, מכפלה ריקה ובטח זה עם מספר המחרוזות - כולם <strong>מאפשרים</strong> לי להגדיר {% equation %}0^{0}=1{% endequation %} ולהרגיש טוב עם זה.

בהגדרה הרקורסיבית, {% equation %}0^{0}=1{% endequation %} הוא פשוט בחירה לגיטימית למקרה הבסיס, ואחר כך מקבלים {% equation %}0^{n}=0{% endequation %} לכל {% equation %}n{% endequation %} טבעי, כך שלא נגמרת אף סתירה. מה שנכון הוא שההגדרה הרקורסיבית הייתה עובדת גם אם הייתי בוחר {% equation %}0^{0}=142342{% endequation %} שנראה שרירותי לגמרי; זה לא כל כך שונה מלומר שאני יכול להגדיר את {% equation %}\frac{0}{0}{% endequation %} להיות מה שבא לי. ההבדל הוא שבהגדרה הרקורסיבית אני רוצה לדבר מראש על הגדרה לכל {% equation %}x{% endequation %}: אני אומר <strong>באופן כללי</strong> ש-{% equation %}x^{0}=1{% endequation %} וש-{% equation %}x^{n+1}=x\times x^{n}{% endequation %}. אני לא טורח להחריג את 0 החוצה, כי אין סיבה לעשות את זה - ההגדרה עובדת טוב גם יחד איתו.

בגישת "המכפלה הריקה" מה שקורה הוא ש-{% equation %}0^{0}{% endequation %} מייצג את "המכפלה הריקה" של קבוצה שאין בה שום דבר. אין הבדל בין {% equation %}1^{0}{% endequation %} ובין {% equation %}0^{0}{% endequation %} מהבחינה הזו - כשהקבוצה ריקה, הזהות של האיבר ש<strong>פוטנציאלית</strong> יכל להיות בה לא משפיעה עלינו. זה מאוד דומה לגישת "המחרוזת מאורך 0" שבה לא משנה מי האותיות ש<strong>פוטנציאלית</strong> יכלו להיות חלק מהמחרוזת. אם כן, {% equation %}0^{0}=1{% endequation %} זו ההגדרה הטבעית ביותר שלנו.

אז למה לא הכל טוב? כי יש גישות אחרות ל-{% equation %}0^{0}{% endequation %} שבהן אם הוא יהיה שווה ל-1, זה לא יסתדר עם דברים אחרים. הנה דוגמא מתחום החשבון הדיפרנציאלי והאינטגרלי (חדו"א): בואו נסתכל למשל על הפונקציה {% equation %}f\left(x\right)=x^{x}{% endequation %}. כאשר אנחנו מציבים בה ערכים קטנים יותר ויותר של {% equation %}x{% endequation %} חיובי אנחנו מתקרבים יותר ויותר למספר 1 - תנסו ותראו! פורמלית כותבים את זה, {% equation %}\lim_{x\to}x^{x}=1{% endequation %}. העניין הוא שאפשר גם לעשות משהו אחר לגמרי. למשל, בואו נגדיר {% equation %}g\left(x\right)=2^{-\frac{1}{x}}{% endequation %} ו-{% equation %}h\left(x\right)=-x{% endequation %}. לא קשה לראות שכאשר {% equation %}x{% endequation %} מתקרב ל-0, אז שתי הפונקציות הללו מתקרבות ל-0 גם כן. מצד שני, {% equation %}\lim_{x\to0}g\left(x\right)^{h\left(x\right)}=2{% endequation %} פשוט כי {% equation %}g\left(x\right)^{h\left(x\right)}=\left(2^{\left(-\frac{1}{x}\right)}\right)^{-x}=2^{\frac{x}{x}}=2{% endequation %}. את התעלול הזה אפשר לעשות לא רק עם 2 אלא עם כל מספר שנרצה, ולכן לכל {% equation %}a{% endequation %} אפשר למצוא פונקציות {% equation %}g,h{% endequation %} כך ש-{% equation %}\lim_{x\to0}g\left(x\right)=\lim_{x\to0}h\left(x\right)=0{% endequation %} אבל {% equation %}\lim_{x\to0}g\left(x\right)^{h\left(x\right)}=a{% endequation %}.

זו התנהגות <strong>שונה</strong> ממה שקורה בדרך כלל בגבולות. אם {% equation %}\lim_{x\to0}g\left(x\right)=a{% endequation %} ו-{% equation %}\lim_{x\to0}h\left(x\right)=b{% endequation %} עבור {% equation %}a,b{% endequation %} חיוביים, אז {% equation %}\lim_{x\to0}g\left(x\right)^{h\left(x\right)}=a^{b}{% endequation %}. אין אפשרות להתחכם. רק במקרה שבו שתי הפונקציות הללו שואפות לאפס לא ניתן לדעת כלום על מה יהיה הגבול בסופו של דבר. לכן מי שמתעסק בחדו"א לא ישמח בכלל להגדיר {% equation %}0^{0}=1{% endequation %}; מבחינתו אין שום הגיון בהגדרה כזו.

ומה עם {% equation %}x^{0}{% endequation %} כאשר {% equation %}x{% endequation %} הוא חיובי? לגבי זה גם איש החדו"א יסכים שההגדרה {% equation %}x^{0}=1{% endequation %} עובדת היטב. אני לא מכיר מקום כלשהו במתמטיקה שבו {% equation %}x^{0}=1{% endequation %} הוא <strong>לא</strong> הגיוני כאשר {% equation %}x{% endequation %} הוא חיובי והמשמעות של חזקה היא המשמעות הרגילה שלה.

אז לסיכום: לומר ש-{% equation %}x^{0}=1{% endequation %} זו לא סתם הגדרה שרירותית; יש בה הגיון והיא די מתבקשת. מצד שני, זו עדיין הגדרה ולא חוק טבע. יותר מאשר מעניין אותי לשכנע אתכם שהיא נכונה, אני רוצה לשכנע אתכם שהיא <strong>מעניינת</strong>.