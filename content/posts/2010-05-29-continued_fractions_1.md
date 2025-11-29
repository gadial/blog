---
id: 514
title: "שברים משולבים, ולמה הם מגניבים"
date: 2010-05-29 16:31:47
layout: post
categories: 
  - תורת המספרים
tags: 
  - האלגוריתם האוקלידי
  - שברים משולבים
social_media_share: true
---
אוהבים לטעון שהמתמטיקה היא כל כולה ערב רב של נוסחאות מפחידות בעלות משמעות לא ברורה. אני חושב שזה מאוד לא מדויק, אבל מדי פעם אכן מתפלקת לה איזו נוסחה שנראית מפחיד גם למי שכבר יש לו נסיון בסיסי כלשהו במתמטיקה. מה שהפחיד אותי בשעתו היו <a href="http://he.wikipedia.org/wiki/%D7%A9%D7%91%D7%A8_%D7%9E%D7%A9%D7%95%D7%9C%D7%91">השברים המשולבים</a> - שברים מהצורה החביבה {% equation %}\frac{1}{1+\frac{1}{3+\frac{1}{1+\frac{1}{4}}}}{% endequation %}. כשרואים דבר כזה, התגובה המיידית של אדם שפוי צריכה להיות "מה, לעזאזל...". בפוסט הזה אני רוצה להסביר מה, לעזאזל. מכיוון שאני חושב שבנושא הזה הדרך הטובה ביותר לדעת מה לעזאזל היא ללכלך את הידיים, חלקו השני של הפוסט יהיה יותר "חישובי" מהרגיל - אך חישובים שלדעתי הם יפים ומעניינים (ובלי לעשות אותם "בידיים"קצת קשה לראות את זה, לדעתי).

בראש ובראשונה, הדבר הזה הוא בסך הכל שבר רגיל. תלמיד כיתה ה' אמור כבר להיות מסוגל להבין מהו ולחשב את ערכו. במקרה של השבר שלעיל, למשל, פשוט צריך לעשות סדרה של חיבורים. {% equation %}1+\frac{1}{4}=\frac{5}{4}{% endequation %} ו-{% equation %}\frac{1}{\frac{5}{4}}=\frac{4}{5}{% endequation %} כך שהשבר שווה ל-{% equation %}\frac{1}{1+\frac{1}{3+\frac{4}{5}}}{% endequation %}; וכעת {% equation %}3+\frac{4}{5}=\frac{19}{5}{% endequation %} כך שנקבל שהשבר שווה ל-{% equation %}\frac{1}{1+\frac{5}{19}}{% endequation %}; ולסיום נקבל שהוא שווה ל-{% equation %}\frac{19}{24}{% endequation %}. מה שלא ברור הוא למה לבחור בדרך ייצוג כה מסורבלת ל-{% equation %}\frac{19}{24}{% endequation %}, והתשובה הבסיסית היא - כי זו דרך הייצוג הטבעית והנכונה ביותר למספרים. לא מאמינים? חכו חכו.

ראשית בואו נוותר על הייצוג המסורבל והמזוויע טיפוגרפית. שבר משולב כללי הוא מהצורה {% equation %}a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\dots}}{% endequation %} (כמובן שאפשר להגדיר שברים משולבים בצורה כללית יותר כך שבמונים יהיו מספרים השונים מ-1, אך זה מסבך את האנליזה ואינו הכרחי כאן ולכן אשתמש בהגדרה המצומצמת) ואת אותו דבר אפשר לתאר בצורה ברורה בעזרת הסימון {% equation %}a_{0}+\frac{1}{a_{1}+}\dots\frac{1}{a_{n}}{% endequation %}. למשל, השבר המשולב שלעיל מיוצג בידי {% equation %}\frac{1}{1+}\frac{1}{3+}\frac{1}{1+}\frac{1}{4}{% endequation %}.

השאלה הראשונה שאני רוצה לעסוק בה היא זו - נניח שיש לנו מספר רציונלי, {% equation %}\frac{a}{b}{% endequation %}; איך מציגים אותו כשבר משולב? למשל, {% equation %}\frac{19}{24}{% endequation %}. מה עושים כדי לתת לו את הצורה ה"קנונית"? כדי לסבך עוד קצת את העניינים אעדיף לדבר על שבר שגדול מ-1, נניח {% equation %}\frac{67}{24}{% endequation %}. את הייצור הזה אפשר לייצג כ-{% equation %}2+\frac{19}{24}{% endequation %}, כך ש-{% equation %}a_{0}=2{% endequation %} במקרה שלנו. מה עכשיו? אנחנו רוצים להחליף את ה-{% equation %}\frac{19}{24}{% endequation %} בגורם מהצורה אחד חלקי משהו, אז ראשית כל נכתוב {% equation %}\frac{19}{24}=\frac{1}{\frac{24}{19}}{% endequation %}, וכעת במכנה יש לנו שוב שבר מדומה ואפשר לפרק אותו לחלק ממשי וחלק שברי: {% equation %}\frac{1}{1+\frac{5}{19}}{% endequation %} (כלומר {% equation %}a_{1}=1{% endequation %}). נחזור על התעלול שוב עבור {% equation %}\frac{5}{19}{% endequation %} ונקבל {% equation %}a_{2}=3{% endequation %} ו"שארית"של {% equation %}\frac{4}{5}{% endequation %}; וכשנטפל ב-{% equation %}\frac{5}{4}{% endequation %} נקבל {% equation %}1+\frac{1}{4}{% endequation %} והמשחק יסתיים. זה תהליך שיטתי ופשוט למדי, וייתכן שלחדי העין שבכם הוא הזכיר תהליך אחר במתמטיקה, שידוע עוד מימי היוונים הקדמונים - האלגוריתם האוקלידי.

בהינתן שני מספרים טבעיים {% equation %}a,b{% endequation %}, האלגוריתם האוקלידי מוצא את המחלק המשותף המקסימלי שלהם: מספר טבעי {% equation %}d{% endequation %} שמחלק הן את {% equation %}a{% endequation %} והן את {% equation %}b{% endequation %} והוא הגדול ביותר בעל תכונה זו. עבור {% equation %}67{% endequation %} ו-{% equation %}24{% endequation %} המחלק המקסימלי הזה הוא המספר הלא מרשים {% equation %}1{% endequation %} (במקרה כזה אומרים ש-67 ו-24 הם "זרים"), אבל מן הסתם יש דוגמאות מעניינות יותר - למשל המחלק המשותף המקסימלי של {% equation %}78{% endequation %} ו-{% equation %}42{% endequation %} הוא {% equation %}6{% endequation %}.

כדי למצוא מחלק מקסימלי אפשר לעשות דברים מטופשים כמו לעבור על כל המספרים הקטנים מ-{% equation %}a{% endequation %} ו-{% equation %}b{% endequation %} ולבדוק אם הם מחלקים אותם וכדומה, אבל מבחינה חישובית זו שיטה איטית ומייגעת. האלגוריתם האוקלידי, לעומת זאת, פועל מהר מאוד (פורמלית - זמן לוגריתמי בגודל המספרים המעורבים). למעשה, היעילות של האלגוריתם האוקלידי היא הבסיס לתורת המספרים האלגוריתמית; רבים מהחישובים שמתבצעים בתורה זו מסתמכים ברמה זו או אחרת על האלגוריתם האוקלידי (בפרט על גרסה מורחבת שלו, שמאפשרת למצוא {% equation %}x,y{% endequation %} שלמים (לא בהכרח חיוביים) כך ש-{% equation %}ax+by=d{% endequation %}, כש-{% equation %}d{% endequation %} הוא המחלק המשותף המקסימלי) ואלמלא הוא היה יעיל, מספר הדברים שניתן לבצע ביעילות היה קטן משמעותית (בפרט, שימוש קריטי שלו הוא למציאת הופכי מודולו {% equation %}n{% endequation %} של מספרים, מה שהוא הבסיס למימוש פעולות חשבון ב-{% equation %}\mathbb{Z}_{n}^{*}{% endequation %} - אחרת, אין אפשרות לבצע חלוקה).

הרעיון שמאחורי האלגוריתם האוקלידי פשוט מאוד: בהינתן {% equation %}a,b{% endequation %} (נניח ש-{% equation %}a{% endequation %} גדול יותר מ-{% equation %}b{% endequation %}) אפשר לחלק את {% equation %}a{% endequation %} ב-{% equation %}b{% endequation %} ולקבל שארית {% equation %}r{% endequation %} (במילים אחרות, למצוא {% equation %}q,r{% endequation %} כך ש-{% equation %}a=qb+r{% endequation %} ו-{% equation %}0&lt;r&lt;b{% endequation %}). האבחנה המרכזית היא שהמחלק המשותף המקסימלי של {% equation %}a,b{% endequation %} הוא גם המחלק המשותף המקסימלי של {% equation %}b,r{% endequation %} (למה?) ולכן אפשר להפעיל את האלגוריתם באופן רקורסיבי על {% equation %}b,r{% endequation %}, כשתנאי העצירה שלנו הוא שאם {% equation %}b{% endequation %} מחלק את {% equation %}a{% endequation %} ללא שארית, אז המחלק המשותף המקסימלי שלהם הוא {% equation %}b{% endequation %} עצמו.

בואו ונראה איך זה עובד עבור {% equation %}67{% endequation %} ו-{% equation %}24{% endequation %}:

{% equation %}67=2\times24+19{% endequation %}

{% equation %}24=1\times19+5{% endequation %}

{% equation %}19=3\times5+4{% endequation %}

{% equation %}5=1\times4+1{% endequation %}

{% equation %}4=4\times1+0{% endequation %}

ובשלב האחרון סיימנו: קיבלנו {% equation %}a=4,b=1{% endequation %} וראינו ש-{% equation %}b{% endequation %} מחלק את {% equation %}a{% endequation %} ללא שארית. אלא שמה שמעניין כאן הוא דווקא אותם ערכי {% equation %}q{% endequation %} שהצטברו במהלך הדרך (המספרים שמשמאל לסימן ה-{% equation %}\times{% endequation %} בכל שורה) - הסתכלו עליהם - האם הם נראים מוכרים?

הבה ונציג את החלוקות שמבצע האלגוריתם האוקלידי בדרך אחרת. במקום לדבר על חלוקה עם שארית, נעבוד ישירות עם שברים:

{% equation %}\frac{67}{24}=2+\frac{19}{24}{% endequation %}

{% equation %}\frac{24}{19}=1+\frac{5}{19}{% endequation %}

{% equation %}\frac{19}{5}=3+\frac{4}{5}{% endequation %}

{% equation %}\frac{5}{4}=1+\frac{1}{4}{% endequation %}

{% equation %}\frac{4}{1}=4+0{% endequation %}

וזה כבר מאוד מזכיר את התהליך שתיארתי למעלה, של בניית השבר המשולב עבור {% equation %}\frac{19}{24}{% endequation %}. המסקנה היא ש-{% equation %}\frac{67}{24}{% endequation %} מתואר בידי השבר המשולב {% equation %}2+\frac{1}{1+}\frac{1}{3+}\frac{1}{1+}\frac{1}{4}{% endequation %}, ושבאופן כללי אפשר למצוא את השבר המשולב עבור {% equation %}\frac{a}{b}{% endequation %} ביעילות באמצעות האלגוריתם האוקלידי - ובגלל שהעצירה של האלגוריתם האוקלידי מובטחת, גם העצירה של בניית השבר המשולב מובטחת. מה שעוד לא ברור כאן הוא שאם מספר מיוצג בידי שבר משולב, הייצוג הזה הוא יחיד, ולא ייתכן ששני שברים משולבים ייצגו את אותו המספר; גם את זה לא מסובך להוכיח אך ההוכחה טכנית ואפסח עליה.

עד כה לא ממש ברור ממה ההתלהבות הגדולה. אז כן, מצאנו דרך חדשה ומופרעת להציג שברים, אך במה היא טובה יותר מלכתוב סתם {% equation %}\frac{a}{b}{% endequation %}? החלק המעניין מתחיל כשאנו רוצים לייצג באמצעות שברים משולבים מספרים שלא ניתן לייצג באמצעות שברים רגילים, כלומר מספרים אי רציונליים. לצורך כך יהיה הכרחי להרחיב קצת את ההגדרה של שברים משולבים, שכן לא קשה לראות שכרגע כל שבר משולב שאנו מדברים עליו הוא מספר רציונלי (פשוט "פותחים"אותו באופן שעליו כבר דיברתי קודם).

אם כן, מה שנעשה הוא להרשות לתהליך של יצירת השבר להימשך עד אינסוף. במקום שנייצג שבר משולב עם סדרה סופית {% equation %}a_{0}+\frac{1}{a_{1}+}\dots\frac{1}{a_{n}}{% endequation %}, פשוט נרשה לסדרה להיות אינסופית: {% equation %}a_{0}+\frac{1}{a_{1}+}\dots{% endequation %}. למי שמטרידה אותו השאלה איך אפשר לתת משמעות פורמלית לכזה דבר, התשובה פשוטה: {% equation %}a_{0}+\frac{1}{a_{1}+}\dots=\lim_{n\to\infty}a_{0}+\frac{1}{a_{1}+}\dots\frac{1}{a_{n}}{% endequation %}. במילים אחרות, אם יש לנו סדרה אינסופית {% equation %}a_{0},a_{1},\dots{% endequation %} אנחנו יכולים לקבל ממנה סדרה אינסופית של מספרים רציונליים שמתקבלים מכך ש"קוטמים"את השבר המשולב בכל פעם בשלב מתקדם יותר. כמובן שלא ברור מיידית שהסדרה הזו אכן שואפת למספר ספציפי יחיד; כדי להבין יותר טוב מה הולך כאן, נרצה קודם כל להבין את סדרת הקירובים שמגדיר שבר משולב. ההמשך יהיה יחסית טכני (אם כי לטעמי מעניין מאוד), ואת השורה התחתונה כבר אכתוב בפוסט הבא, לטובת אלו שלא יצליחו לעקוב.

באופן כללי, אם {% equation %}a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}+}\dots{% endequation %} הוא שבר משולב (סופי או אינסופי) אפשר להגדיר סדרה {% equation %}\frac{A_{0}}{B_{0}},\frac{A_{1}}{B_{1}},\frac{A_{2}}{B_{2}},\dots{% endequation %} של הקירובים המתקבלים משלבי הביניים: {% equation %}\frac{A_{0}}{B_{0}}=a_{0}{% endequation %}, ו-{% equation %}\frac{A_{1}}{B_{1}}=a_{0}+\frac{1}{a_{1}}{% endequation %} וכן הלאה. השאלה המעניינת ביותר כאן לטעמי היא "האם אפשר לכתוב את {% equation %}A_{n},B_{n}{% endequation %} בצורה פשוטה כפונקציות של {% equation %}a_{0},\dots,a_{n}{% endequation %}?" והתשובה המפתיעה היא שלא רק שאפשר לעשות את זה, אלא גם ש-{% equation %}A_{n}{% endequation %} ו-{% equation %}B_{n}{% endequation %} מאוד, מאוד דומים.

בואו נראה לאט לאט כיצד נבנה שבר משולב. בשלב הראשון יש לנו {% equation %}\frac{a_{0}}{1}{% endequation %} ותו לא. בשלב השני יש לנו את {% equation %}a_{0}+\frac{1}{a_{1}}{% endequation %}; כדי לראות למה זה שווה אנחנו מבצעים מכנה משותף ומקבלים {% equation %}\frac{a_{0}a_{1}+1}{a_{1}}{% endequation %}. בשלב השלישי יש לנו {% equation %}a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}}}{% endequation %} וכאן המכנה המשותף נוצר בשני שלבים: ראשית כל מתקבל {% equation %}a_{0}+\frac{1}{\frac{a_{1}a_{2}+1}{a_{2}}}{% endequation %}, ולאחר מכן המכנה "מתהפך", מקבלים {% equation %}a_{0}+\frac{a_{2}}{a_{1}a_{2}+1}{% endequation %}, ולבסוף מתקבל {% equation %}\frac{a_{0}a_{1}a_{2}+a_{0}+a_{2}}{a_{1}a_{2}+1}{% endequation %}.

חדי העין בוודאי שמו לב לדמיון שבין המונה של {% equation %}a_{0}+\frac{1}{a_{1}}{% endequation %} ובין <strong>המכנה</strong> של {% equation %}a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}}{% endequation %}: הראשון הוא {% equation %}a_{0}a_{1}+1{% endequation %}, השני הוא {% equation %}a_{1}a_{2}+1{% endequation %}. זהו כמובן אינו מקרה: הרי המכנה של {% equation %}a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}}{% endequation %} התקבל מהמונה של {% equation %}a_{1}+\frac{1}{a_{2}}{% endequation %}. זכרו - כדי לחשב את {% equation %}a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}}{% endequation %} אמרנו "בואו קודם כל נשכח מה-{% equation %}a_{0}{% endequation %} ונסתכל על המכנה {% equation %}a_{1}+\frac{1}{a_{2}}{% endequation %}", אבל מכנה זה הוא בעצמו שבר משולב "רגיל". אחרי שגמרנו לחשב אותו ולהביא אותו לצורה {% equation %}\frac{x}{y}{% endequation %} ביצענו בו "היפוך" שבו הוחלפו המונה והמכנה.

ההבנה הזו, שהמכנה של שבר משולב הוא בעצם המונה של שבר משולב קצת יותר פשוט, מאפשרת לנו לתאר בצורה קצת יותר נחמדה את המונה והמכנה. נשתמש בסימון {% equation %}\left[a_{0},a_{1},\dots,a_{n}\right]{% endequation %} כדי לתאר את המונה של השבר המשולב, ועכשיו יש לנו תיאור יפה לקירובים: {% equation %}\frac{A_{n}}{B_{n}}=\frac{\left[a_{0},\dots,a_{n}\right]}{\left[a_{1},\dots,a_{n}\right]}{% endequation %}. זה עדיין לא עוזר לנו להבין איך בדיוק נראית המפלצת שמיוצגת על ידי {% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %}, אבל זו התחלה טובה.

כעת בואו ונתבונן שניה בשבר המשולב {% equation %}a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}+}\dots\frac{1}{a_{n}}{% endequation %}. מצד אחד, אפשר לכתוב אותו כ-{% equation %}\frac{\left[a_{0},\dots,a_{n}\right]}{\left[a_{1},\dots,a_{n}\right]}{% endequation %} כפי שכבר אמרתי. מצד שני, אפשר לכתוב אותו כ-{% equation %}a_{0}+\frac{\left[a_{2},\dots,a_{n}\right]}{\left[a_{1},\dots,a_{n}\right]}{% endequation %}, שכן אפשר "לחשב עד הסוף" את {% equation %}a_{1}+\frac{1}{a_{2}+}\dots\frac{1}{a_{n}}{% endequation %} ולבסוף לבצע היפוך שלו. מכאן מתקבלת בקלות הנוסחה הבאה: {% equation %}\left[a_{0},\dots,a_{n}\right]=a_{0}\left[a_{1},\dots,a_{n}\right]+\left[a_{2},\dots,a_{n}\right]{% endequation %}. זו כבר ההתחלה של הגיון בשגעון - ראשית, כעת יש לנו דרך רקורסיבית פשוטה לחשב את {% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %}; אבל שנית, כעת נוכל להוכיח באינדוקציה תיאור כללי ולא רקורסיבי של המבנה של {% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %} שהתגלה, כמו מיליארד דברים אחרים, בידי אוילר.

הכלל נשמע טיפה מוזר ומפחיד בשמיעה ראשונה, אבל עברנו את פרעה ואת "<a href="http://www.gadial.net/2010/05/26/cancelling_math/">איך בוטלה המתמטיקה</a>"ונעבור גם את זה: {% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %} הוא סכום של מכפלות שמתקבלות באופן הבא: ראשית, המכפלה {% equation %}a_{1}a_{2}\cdots a_{n}{% endequation %}. שנית, המכפלה {% equation %}a_{1}a_{2}\cdots a_{n}{% endequation %} כשהוסר ממנה זוג איברים סמוכים (נניח, {% equation %}a_{3}a_{4}{% endequation %} הוסר ממנה) - כל המכפלות האפשריות שיכולות להתקבל מהסרת זוג כזה משתתפות בסכום. שלישית, כל המכפלות שמתקבלות מהסרת <strong>שני</strong> זוגות זרים (כלומר, למשל, {% equation %}a_{2}a_{3}{% endequation %} ו-{% equation %}a_{7}a_{8}{% endequation %}) וכן הלאה. אם כל האיברים הוסרו ממכפלה היא הופכת להיות "המכפלה הריקה" - 1 (שכן 1 הוא האיבר הנייטרלי לכפל, ולכן הוא מתאים רעיונית לייצוג מכפלה ריקה כשם ש-0 מתאים רעיונית לייצוג סכום ריק).

דוגמאות פשוטות עוזרות כמובן להבין. {% equation %}\left[a_{0}\right]=a_{0}{% endequation %} שכן יש לנו את המכפלה של "כל" האיברים, וזהו (אין זוגות סמוכים שאפשר להוריד). {% equation %}\left[a_{0}a_{1}\right]=a_{0}a_{1}+1{% endequation %} שכן יש לנו את המכפלה של כל האיברים {% equation %}a_{0}a_{1}{% endequation %} ואת המכפלה הריקה {% equation %}1{% endequation %}. {% equation %}\left[a_{0},a_{1},a_{2}\right]=a_{0}a_{1}a_{2}+a_{0}+a_{2}{% endequation %}, כש-{% equation %}a_{1}{% endequation %} לא מופיע בסכום לבדו שכן אין זוג <strong>סמוך</strong> שניתן להוריד ויותיר רק אותו. לבסוף, הנה דוגמה יותר מורכבת:

{% equation %}\left[a_{0},a_{1},a_{2},a_{3},a_{4}\right]=a_{0}a_{1}a_{2}a_{3}a_{4}+{% endequation %}

{% equation %}a_{0}a_{1}a_{2}+a_{0}a_{1}a_{4}+a_{1}a_{2}a_{3}+a_{2}a_{3}a_{4}+{% endequation %}

{% equation %}a_{0}+a_{2}+a_{4}{% endequation %}

כש-{% equation %}a_{2}{% endequation %} התקבל מכך שהסרנו את הזוגות {% equation %}a_{0}a_{1}{% endequation %} ו-{% equation %}a_{3}a_{4}{% endequation %}.

מבלבל? כן, אבל לא קשה כל כך להוכחה באינדוקציה בעזרת הנוסחה {% equation %}\left[a_{0},\dots,a_{n}\right]=a_{0}\left[a_{1},\dots,a_{n}\right]+\left[a_{2},\dots,a_{n}\right]{% endequation %}. את הבסיס (עבור {% equation %}\left[a_{0}\right]{% endequation %} ו-{% equation %}\left[a_{0}a_{1}\right]{% endequation %}) אפשר לראות ישירות; באופן כללי, הבה ונראה מה קורה עם {% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %}. ראשית, הגורם {% equation %}\left[a_{2},\dots,a_{n}\right]{% endequation %} תופס את כל המחוברים שהתקבלו על ידי הסרת הזוג {% equation %}a_{0}a_{1}{% endequation %} ואולי עוד דברים, כך שהגורם הזה בסדר; ואילו {% equation %}a_{0}\left[a_{1},\dots,a_{n}\right]{% endequation %} תופס את כל הגורמים שהתקבלו ללא הסרת {% equation %}a_{0}{% endequation %} מההתחלה, ומכיוון שאם מסירים את {% equation %}a_{0}{% endequation %} זה חייב להיות במסגרת הזוג {% equation %}a_{0}a_{1}{% endequation %} תפסנו את כל המקרים.

יופי, אז יש לנו תיאור די מפורש של {% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %}; מה עכשיו? ראשית, עכשיו ברור ש-{% equation %}\left[a_{0},\dots,a_{n}\right]{% endequation %} הוא ביטוי סימטרי, במובן זה שהוא זהה ל-{% equation %}\left[a_{n},\dots,a_{0}\right]{% endequation %}, ולכן את נוסחת הנסיגה {% equation %}\left[a_{0},\dots,a_{n}\right]=a_{0}\left[a_{1},\dots,a_{n}\right]+\left[a_{2},\dots,a_{n}\right]{% endequation %} אפשר לכתוב גם מהסוף להתחלה, בתור {% equation %}\left[a_{n},\dots,a_{0}\right]=a_{n}\left[a_{n-1},\dots,a_{0}\right]+\left[a_{n-2},\dots,a_{0}\right]{% endequation %}. עכשיו, מכיוון ש-{% equation %}A_{n}=\left[a_{0},\dots,a_{n}\right]{% endequation %} ו-{% equation %}B_{n}=\left[a_{1},\dots,a_{n}\right]{% endequation %}, קיבלנו את נוסחת הנסיגה {% equation %}A_{n}=a_{n}A_{n-1}+A_{n-2}{% endequation %} ו-{% equation %}B_{n}=a_{n}B_{n-1}+B_{n-2}{% endequation %}. אותה נוסחת נסיגה מתארת הן את המונה והן את המכנה וזה כמובן לא מפתיע בהתחשב בכך שכבר אמרתי שהם בעצם אותו הדבר.

מנוסחאות הנסיגה הללו אפשר לגזור נוסחה שקושרת את {% equation %}A_{n},B_{n}{% endequation %} והיא לב-לבו של העסק. הבה ונסמן ב-{% equation %}\Delta_{n}{% endequation %} את הביטוי הבא: {% equation %}\Delta_{n}=A_{n}B_{n-1}-A_{n-1}B_{n}{% endequation %}. למה הוא שווה? מסתבר שניתן לחשב אותו במדוייק וערכו מאוד פשוט. כדי לראות זאת, נשתמש בנוסחת הנסיגה ונקבל את הפיתוח הבא:

{% equation %}\Delta_{n}=A_{n}B_{n-1}-A_{n-1}B_{n}=\left(a_{n}A_{n-1}+A_{n-2}\right)B_{n-1}-A_{n-1}\left(a_{n}B_{n-1}+B_{n-2}\right)={% endequation %}

{% equation %}B_{n-1}A_{n-2}-A_{n-1}B_{n-2}=-\Delta_{n-1}{% endequation %}

ולא קשה לראות כי {% equation %}\Delta_{1}=A_{1}B_{0}-A_{0}B_{1}=1{% endequation %}, כך שקיבלנו בסך הכל ש-{% equation %}\Delta_{n}=\left(-1\right)^{n-1}{% endequation %}. הבה ונכתוב את הנוסחה במפורש:

{% equation %}A_{n}B_{n-1}-A_{n-1}B_{n}=\left(-1\right)^{n-1}{% endequation %}

זו לדעתי דוגמה לנוסחה "יפה", ובכלל - כל החיפוש אחר התכונות של {% equation %}A_{n},B_{n}{% endequation %} מהווה לטעמי דוגמה למתמטיקה שהיא מצד אחד טכנית וחשבונית מאוד, ומצד שני היא יפה ואף יצירתית.

טוב, חדל התלהבות, נשאלת השאלה מה יצא לנו מכל זה. התשובה היא שיצא לנו המון - עכשיו אנחנו יודעים לתאר היטב את ההתנהגות של הסדרה {% equation %}\frac{A_{0}}{B_{0}},\frac{A_{1}}{B_{1}},\dots{% endequation %}. בפרט, אנחנו יודעים לתאר בקלות את ההפרש בין שני גורמים סמוכים. נסו לחשוב שנייה מדוע, ואז הציצו בשורה הבאה:

{% equation %}\frac{A_{n}}{B_{n}}-\frac{A_{n-1}}{B_{n-1}}=\frac{A_{n}B_{n-1}-A_{n-1}B_{n}}{B_{n}B_{n-1}}=\frac{\left(-1\right)^{n-1}}{B_{n}B_{n-1}}{% endequation %}.

מכיוון ש-{% equation %}B{% endequation %}-ים חיוביים תמיד, נובע שאם {% equation %}n{% endequation %} אי זוגי, אז {% equation %}\frac{A_{n}}{B_{n}}{% endequation %} גדול מ-{% equation %}\frac{A_{n-1}}{B_{n-1}}{% endequation %} (הפרשם חיובי) ואחרת הוא קטן ממנו. מכאן שסדרת הקירובים "מזפזפת" מעלה ומטה. אבל האם היא נרגעת? ובכן, בואו ננסה לראות מה קורה כשמשווים איבר לא לקודמו, אלא לזה שלפניו, כלומר מנסים לחשב את {% equation %}\frac{A_{n}}{B_{n}}-\frac{A_{n-2}}{B_{n-2}}{% endequation %}. הדרך הפשוטה ביותר לעשות זאת היא באמצעות תעלול נפוץ מאוד בחשבון: להוסיף ולהחסיר את אותו איבר. נקבל:

{% equation %}\frac{A_{n}}{B_{n}}-\frac{A_{n-2}}{B_{n-2}}=\left(\frac{A_{n}}{B_{n}}-\frac{A_{n-1}}{B_{n-1}}\right)+\left(\frac{A_{n-1}}{B_{n-1}}-\frac{A_{n-2}}{B_{n-2}}\right)=\frac{\left(-1\right)^{n-1`}}{B_{n}B_{n-1}}+\frac{\left(-1\right)^{n-2}}{B_{n-1}B_{n-2}}=\frac{\left(-1\right)^{n-1}}{B_{n-1}}\left[\frac{1}{B_{n}}-\frac{1}{B_{n-2}}\right]{% endequation %}

האיבר בסוגריים המרובעים הוא ללא ספק שלילי, כי הוא מכיל משהו חיובי במכנה ו-{% equation %}B_{n-2}-B_{n}{% endequation %} במונה, אבל ב-{% equation %}B_{n}{% endequation %} גדול מ-{% equation %}B_{n-2}{% endequation %} כי הוא מכיל את {% equation %}B_{n-2}{% endequation %} כחלק מהסכום שלו (מדוע?). מסקנה: עבור ערכים זוגיים של {% equation %}n{% endequation %}, אנחנו מקבלים שההפרש כולו חיובי, ולכן הסדרה של ה-{% equation %}\frac{A_{n}}{B_{n}}{% endequation %}-ים הזוגיים היא עולה, ואילו סדרת ה-{% equation %}\frac{A_{n}}{B_{n}}{% endequation %}-ים האי זוגיים היא יורדת; וסדרת האיברים הזוגיים חסומה מלמעלה על ידי סדרת האיברים האי זוגיים (ובאופן סימטרי, סדרת האיברים האי זוגיים חסומה מלמטה על ידי סדרת האיברים הזוגיים). כאן נכנס לתמונה משפט בסיסי מחשבון אינפיניטסימלי: אם יש לנו שתי סדרות מספרים, האחת עולה והשנייה יורדת, כך שהמרחק ביניהן שואף לאפס - הן מתכנסות, ולאותו הגבול (במקרה שלנו המרחק הוא {% equation %}\frac{\left(-1\right)^{n-1}}{B_{n}B_{n-1}}{% endequation %} והוא בוודאי שואף לאפס כי ה-{% equation %}B_{n}{% endequation %}-ים שואפים לאינסוף).

הגענו לשורה התחתונה: אם ניקח סדרה <strong>כלשהי</strong> של מספרים טבעיים ונתבונן בשבר המשולב שהיא מגדירה, {% equation %}a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}+}\dots{% endequation %}, נקבל תמיד שהשבר הזה מתכנס למספר ממשי כלשהו. השאלה שנותרה היא האם עבור <strong>כל</strong> מספר ממשי קיים שבר משולב שמתכנס אליו, ואני מניח שאתם מנחשים שהתשובה חיובית. מספיק לדבר על מספרים ממשיים חיוביים, כי עבור מספרים שליליים השינוי היחיד שיידרש הוא שהאיבר {% equation %}a_{0}{% endequation %} יהיה שלילי.

ניקח אם כן מספר ממשי {% equation %}\alpha{% endequation %} שהוא אי רציונלי (ברציונליים כבר טיפלנו). אפשר לפרק אותו לשני חלקים - החלק השלם {% equation %}a_{0}{% endequation %}, שהוא המספר הטבעי הגדול ביותר שעודנו קטן מ-{% equation %}\alpha{% endequation %}; והחלק השברי, שהוא מספר ממשי חיובי קטן מ-1. מכיוון שהוא קטן מ-1, ניתן לכתוב אותו בתור {% equation %}\frac{1}{\alpha_{1}}{% endequation %}. אם כן: {% equation %}\alpha=a_{0}+\frac{1}{\alpha_{1}}{% endequation %}. אני מניח שאתם מבינים מה יבוא כעת: אם {% equation %}\alpha_{1}{% endequation %} אי רציונלי (אחרת {% equation %}\alpha{% endequation %} היה רציונלי - מדוע?) ולכן נחזור על התעלול גם עבורו ונקבל {% equation %}\alpha=a_{0}+\frac{1}{a_{1}+\frac{1}{\alpha_{2}}}{% endequation %} וכן הלאה וכן הלאה. כל שנשאר להבין הוא האם התוצאה אכן מתכנסת אל {% equation %}\alpha{% endequation %} - ואם כן, כמה מהר?

לשם כך נשים לב לרגע לעובדה שלא באמת השתמשנו במה שעוללנו ל-{% equation %}A_{n},B_{n}{% endequation %} בכך שה-{% equation %}a_{n}{% endequation %}-ים כולם שלמים. זה מאפשר לנו לכתוב את {% equation %}\alpha{% endequation %} בתור "שבר משולב" סופי אם נרשה לאיבר האחרון להיות לא שלם, דהיינו {% equation %}\alpha=\frac{\left[a_{0},a_{1},\dots,a_{n},\alpha_{n+1}\right]}{\left[a_{1},a_{2},\dots,a_{n},\alpha_{n+1}\right]}{% endequation %}. אם נשתמש כאן בנוסחת הנסיגה שכבר מצאנו למונה והמכנה, אז אפשר לכתוב {% equation %}\alpha=\frac{\alpha_{n+1}A_{n}+A_{n-1}}{\alpha_{n+1}B_{n}+B_{n-1}}{% endequation %}. עכשיו, כדי לראות עד כמה {% equation %}\frac{A_{n}}{B_{n}}{% endequation %} הוא קירוב טוב ל-{% equation %}\alpha{% endequation %} נחסר את האחד מהשני ונקבל:

{% equation %}\alpha-\frac{A_{n}}{B_{n}}=\frac{\alpha_{n+1}A_{n}+A_{n-1}}{\alpha_{n+1}B_{n}+B_{n-1}}-\frac{A_{n}}{B_{n}}=\frac{A_{n-1}B_{n}+A_{n}B_{n-1}}{B_{n}\left(\alpha_{n+a}B_{n}+B_{n-1}\right)}=\frac{\left(-1\right)^{n-1}}{B_{n}\left(\alpha_{n+a}B_{n}+B_{n-1}\right)}{% endequation %}

כאן שוב השתמשנו בנוסחה הקסומה {% equation %}A_{n}B_{n-1}-A_{n-1}B_{n}=\left(-1\right)^{n-1}{% endequation %}. ניקח ערך מוחלט לביטוי, ונקבל בסופו של דבר ש:

{% equation %}\left|\alpha-\frac{A_{n}}{B_{n}}\right|&lt;\frac{1}{B_{n}B_{n+1}}{% endequation %} (מאיפה ה-{% equation %}B_{n+1}{% endequation %} צץ פתאום? הוא קטן יותר מהגורם שבתוך הסוגריים במכנה - מדוע?).

ושוב, מכיוון ש-{% equation %}B_{n}{% endequation %} היא סדרה עולה, נובע מכך ש-{% equation %}\frac{A_{n}}{B_{n}}{% endequation %} מתכנסת ל-{% equation %}\alpha{% endequation %}, בדיוק כפי שרצינו. לא רק זה - קצב ההתכנסות הוא ריבועי; אך על כך ארחיב בפוסט הבא.

