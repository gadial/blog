---
id: 70
title: "על הבעייה הלא טריוויאלית של זיהוי תכונה לא טריוויאלית"
date: 2007-10-09 23:01:58
layout: post
categories: 
  - חישוביות
tags: 
  - הוכחות
  - חישוביות
  - משפט רייס
---
<a href="http://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%99%D7%AA_%D7%94%D7%A2%D7%A6%D7%99%D7%A8%D7%94">בעיית העצירה</a>, שראינו ב<a href="http://www.gadial.net/?p=64">פוסטים</a> <a href="http://www.gadial.net/?p=65">קודמים</a>, עוסקת ב"התנהגות" של תוכנית מחשב - או במונח הפורמלי שהשתמשתי בו, של <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%9B%D7%95%D7%A0%D7%AA_%D7%98%D7%99%D7%95%D7%A8%D7%99%D7%A0%D7%92">מכונת טיורינג</a>. הפעם ארצה לעסוק במשהו מעט שונה - בתכונות של הקבוצה שהמכונה יודעת לזהות.

הבעיה פשוטה: בהינתן תכונה של קבוצת מספרים טבעיים, אנחנו רוצים אלגוריתם כלשהו שמקבל כקלט מכונת טיורינג ואומר האם הקבוצה של המספרים שמזוהים על ידי המכונה (כלומר, שעליהם המכונה עוצרת ואומרת "כן") היא בעלת התכונה הזו או לאו. כפי שניתן לנחש, אלגוריתם שכזה לא קיים כמעט אף פעם, ולמשפט שאומר זאת בצורה פורמלית קוראים <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%A9%D7%A4%D7%98_%D7%A8%D7%99%D7%99%D7%A1"><strong>משפט רייס</strong></a>.

ראשית, מהן "תכונות" של קבוצות של מספרים? למשל, "1 שייך לקבוצה" היא תכונה. "כל מספר בקבוצה הוא זוגי" היא תכונה. "קיימים בקבוצה שלושה מספרים x,y,z כך ש-{% equation %}x^3+y^3=z^3{% endequation %}" היא תכונה. הבנתם את העיקרון. הבעיה היא שההגדרות הללו של תכונות הן מופשטות יחסית - קשה "לעבוד" איתן - ולכן אציג הגדרה אלטרנטיבית, שנראית די טיפשית במבט ראשון: תכונה של קבוצות טבעיים היא חלוקה של כל קבוצות הטבעיים (במקרה שלנו, רק של הקבוצות שניתן לזהות בידי מכונת טיורינג) לשתי מחלקות - מחלקת כל הקבוצות שמקיימות את התכונה, ומחלקת כל הקבוצות שלא מקיימות את התכונה.
<p dir="ltr">למשל, התכונה "1 שייך לקבוצה" היא בעצם חלוקה של כל קבוצת הטבעיים (שקיימת מכונת טיורינג שמזהה) לשתי מחלקות - במחלקה הראשונה יש, בין היתר, את הקבוצות {% equation %}\{1\}, \{1,2\},\{1,2,3,\dots\}{% endequation %} וכן הלאה, ובמחלקה השניה את {% equation %}\{2\}, \{2,14\},\{2,3,4,\dots\}{% endequation %} וכדומה.</p>
אלא שלפעמים החלוקה משונה יותר ממה שאפשר לחשוב. נביט בתכונה שנתתי למעלה, של ה-x,y,z שמקיימים משוואה כלשהי - על פי <a href="http://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%A9%D7%A4%D7%98_%D7%94%D7%90%D7%97%D7%A8%D7%95%D7%9F_%D7%A9%D7%9C_%D7%A4%D7%A8%D7%9E%D7%94">המשפט האחרון של פרמה</a> (שהוכח לפני עשור בערך) לא קיימים מספרים כאלו. כלומר, <strong>כל</strong> הקבוצות לא מקיימות את התכונה. במילים אחרות, החלוקה של הקבוצות לשתי מחלקות היא פשוטה במיוחד כאן: מחלקה אחת ריקה, מחלקה שניה מכילה את כל הקבוצות האפשריות של מספרים טבעיים. לחלוקה שכזו קוראים <strong>טריוויאלית</strong>, ולתכונה שמאופיינת על ידי חלוקה שכזו קוראים <strong>טריוויאלית</strong>. המילה "טריוויאלית" כאן, אם כן, אינה טריוויאלית; היא עשויה לתאר הגדרות מחוכמות מאוד, שלחלוטין לא ברור מה הן מגדירות - ועם זאת, כאשר מסתכלים עליהן מזווית הראייה של "כל תכונה היא חלוקה של קבוצות הטבעיים לשתי מחלקות", הטריוויאליות שלהן ברורה הרבה יותר.

אם כן, מה אומר משפט רייס? שלכל תכונה <strong>לא טריוויאלית</strong> S של קבוצות טבעיים (ובניסוחים אחרים - פונקציות, שפות - זה לא חשוב כי הכל שקול) <strong>לא קיים</strong> אלגוריתם שמקבל כקלט מכונת טיורינג M ואומר האם קבוצת המספרים ש-M מקבלת היא בעלת התכונה S.

ההוכחה נחמדה למדי, ואציג אותה כעת. הרעיון המרכזי בה הוא לבצע <strong>רדוקציה</strong> מבעיית העצירה לבעיית זיהוי S הזו. כלומר - להראות שאם אנו יודעים איך לפתור את בעיית זיהוי S, אז באמצעות שימוש באלגוריתם הפותר הזה, אנו מסוגלים לפתור גם את בעיית העצירה - סתירה, כי בעיית העצירה בלתי פתירה.

אבחנה (טריוויאלית) ראשונה היא שבכלל לא חשוב אם אנחנו בודקים את התכונה S או את התכונה ה"הפוכה" לה, התכונה "S לא מתקיים" - מספיק שנראה שאחד משני אלו בלתי אפשרי לבדיקה כדי להראות שגם השני בלתי אפשרי (אם השני היה אפשרי, גם הראשון היה אפשרי - היינו בודקים את השני והופכים את התשובה שלנו מ"כן" ל"לא", ולהפך). לכן אפשר להניח בלי הגבלת הכלליות כי התכונה S לא מתקיימת עבור הקבוצה הריקה.

המילים "בלי הגבלת הכלליות" מופיעות תדיר בטקסטים מתמטיים, והרבה יותר מכך - בעבודות ובמבחנים של סטודנטים שטרם הפנימו מתי בדיוק מותר להשתמש בהן. באופן כללי, מטרתן לומר שההנחה שמבצעים כרגע אמנם אינה בהכרח נכונה, אבל אם היא אינה נכונה אפשר לעבור למקרה אחר, שקול, שבו היא כן נכונה בלי שנפגע בהוכחה. למשל, אם נתנו לנו את התרגיל (הלא טריוויאלי) הבא: "אם x,y,z מספרים זרים שמקיימים {% equation %}x^2+y^2=z^2{% endequation %}, הוכח שקיימים a,b כך שהמספרים מתקבלים באמצעות {% equation %}a^2-b^2,2\cdot ab,a^2+b^2{% endequation %}", אז נוכל לומר בתחילתו "בלי הגבלת הכלליות נניח כי {% equation %}x\le y{% endequation %}", שהרי כרגע x,y הם בסך הכל סימנים שאפשר להחליף ביניהם בחופשיות (לא ידועה לנו אף תכונה של x ש-y לא מקיים, וההפך). אם היה מתקיים {% equation %}x&gt;y{% endequation %}, פשוט היינו מחליפים את הסימן "x" בסימן "y" ולהפך.

אוקיי, אז הנחנו בלי הגבלת הכלליות שהקבוצה הריקה לא מקיימת את S (אחרת נחליף את S במשלימה שלה). מה עכשיו? מכיוון ש-S לא טריוויאלית, קיימת קבוצה ש<strong>כן</strong> מקיימת את S (אחרת, המחלקה "קבוצות שמקיימות את S" הייתה ריקה), ומכיוון שאנו עוסקים רק בקבוצות שקיימת מכונת טיורינג שמזהה אותן, קיימת מכונה שנסמן בתור A שמקבלת את הקבוצה הזו. עכשיו הכיף מתחיל.

אנחנו רוצים לפתור את בעיית העצירה, כלומר לקבל קלט של מכונה M ואיזשהו מספר x ש-M אמורה לרוץ עליו. הרעיון הוא להשתמש ב-M בתור "מסננת" עבור A. אנו יוצרים מכונה חדשה, B, שבנויה כך: היא מקבלת קלט כלשהו a, ואז עושה שני דברים בזה אחר זה:
<ol>
	<li>קודם כל היא מריצה את M על x. כלומר, היא מתעלמת לגמרי מ-a (הקלט שלה) בשלב זה.</li>
	<li>אחרי ש-M מסיימת את ריצתה, היא מריצה את A על a ועונה כמו A.</li>
</ol>
מה הלך כאן?

נניח לרגע ש-M עוצרת על x. אז כל השלב הראשון הוא סתם בזבוז זמן שלא משפיע בכלום על החישוב. מייד אחרי שייגמר, B תתנהג <strong>בדיוק כמו </strong>A על a. כלומר, אם M עוצרת על x הרי שהקבוצה ש-B מזהה היא בדיוק אותה הקבוצה ש-A מזהה - ולכן הקבוצה ש-B מזהה היא בעלת התכונה S.

אבל מה קורה אם M לא עוצרת על x? במקרה הזה, B נשארת תקועה בשלב 1 לנצח. היא לעולם לא תגיע לשלב 2 ולעולם לא תעצור. לכן B לא מקבלת את a, וזאת בלי שום תלות בזהות של a - כלומר, הקבוצה ש-B מזהה היא הקבוצה הריקה - והרי הנחנו (בלי הגבלת הכלליות...) שהקבוצה הריקה אינה בעלת התכונה הזו.

בקיצור, התשובה לשאלה "האם הקבוצה ש-B מקבלת היא בעלת התכונה S" <strong>זהה</strong> לתשובה לשאלה "האם המכונה M עוצרת על x". לכן, כל מה שצריך לעשות הוא להריץ את האלגוריתם הקסום שפותר את בעיית ההכרעה עבור S על המכונה B (שאותה קל לבנות בהינתן A, M, x), לענות כמוהו, וסיימנו.

זוהי דוגמה אחת מני רבות לרדוקציה, והיופי שבה הוא הכלליות הרבה שלה - במחי הוכחה אחת חיסלנו כל שאלה לא טריוויאלית על תכונות הקבוצה שמכונת טיורינג מקבלת - וזו, כאמור, תוצאה ישירה של בעיית העצירה.

אין לי כוונה להתעמק הרבה יותר בתחום לעת עתה, אבל אני מקווה להציג בקרוב רדוקציה נוספת, מעניינת (לטעמי) אף יותר, שבה מראים באמצעות בעיית העצירה את אי הכריעות של בעיה שנראית לחלוטין לא קשורה ממבט ראשון - בעיית הריצוף באמצעות <a href="http://en.wikipedia.org/wiki/Wang_tile">Wang Tiles</a>.