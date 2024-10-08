---
id: 35
title: "הקיים הנעלם - הדוגמה ההסתברותית - מבוא לוגי"
date: 2007-06-30 09:54:24
layout: post
categories: 
  - לוגיקה
tags:
  - הוכחות לא קונסטרוקטיביות
---
אציג כעת דוגמה לשימוש ב<a href="http://he.wikipedia.org/wiki/%D7%AA%D7%95%D7%A8%D7%AA_%D7%94%D7%94%D7%A1%D7%AA%D7%91%D7%A8%D7%95%D7%AA">תורת ההסתברות</a> כדי להוכיח קיום של דבר מה. פרט ל"רווח" המיידי מהדוגמה - עוד הוכחת קיום קונסטרוקטיבית (אם כי מהסוג שמצביע על קיום של משהו שגם חיפוש ממצה יכול למצוא ללא קושי) - זוהי גם הזדמנות לראות דבר מה שאולי אינו מובן מאליו בתחילה: שניתן בעזרת הסתברות להוכיח דברים <strong>בודאות גמורה</strong>.

לרוע המזל, אי אפשר לחמוק מהפרטים הטכניים של ניסוח הבעיה וההוכחה. אלו מכם שאינם מכירים כלל לוגיקה פורמלית והסתברות עלולים שלא להבין את המשך הפוסט (או גרוע מכך - למה הוא מעניין...) אנסה להסביר פחות או יותר את המושגים ולקשר לויקיפדיה, אבל ברור לי שזה לא בהכרח מספיק.

ההוכחה עוסקת ב<a href="http://he.wikipedia.org/wiki/%D7%A4%D7%A1%D7%95%D7%A7_(%D7%9C%D7%95%D7%92%D7%99%D7%A7%D7%94)">פסוקים לוגיים</a> - יצורים שאינם מסובכים במיוחד בפני עצמם, אבל יש להציג אותם בכל זאת. "פסוק" מורכב ממשתנים שיכולים לקבל את הערכים "אמת" ו"שקר". המוטיבציה היא ברצון לפרמל בצורה מתמטית משפטים כמו "השמש זורחת ולא יורד גשם" - משפט כזה ניתן לייצג בתור הפסוק "x וגם לא y", כש-x הוא המשתנה שמייצג את "השמש זורחת", ו-y המשתנה שמייצג את "יורד גשם". אם השמש זורחת (כלומר, x מקבל את הערך "אמת") ובכל זאת יורד גשם (כלומר, גם y מקבל את הערך "אמת") אז ערכו של הפסוק כולו הוא "שקר" (כי השמש אמנם זורחת, אבל לא יורד גשם).

בצורה פורמלית כותבים "x <a href="http://he.wikipedia.org/wiki/%D7%95%D7%92%D7%9D_%28%D7%9C%D7%95%D7%92%D7%99%29">וגם</a> y" בתור {% equation %}x\wedge y{% endequation %}, ואת "x <a href="http://he.wikipedia.org/wiki/OR_%D7%9C%D7%95%D7%92%D7%99">או</a> y" (שפירושו: או x, או y, או שניהם גם יחד) בתור {% equation %}x\vee y{% endequation %}. הכללים ה"חשבוניים" הקשורים לפעולות אלו פשוטים: התוצאה של פעולת "וגם" היא "שקר" אלא אם שני המשתנים מקבלים את הערך "אמת" (ואז היא "אמת"), והתוצאה של פעולת "או" היא תמיד "אמת" אלא אם שני המשתנים מקבלים את הערך "שקר".

יש הרבה צורות לכתוב פסוקים, ולרוב בוחרים צורה "קנונית" מסויימת שמועילה לנו. במקרה שלנו הצורה תהיה ספציפית מאוד:

{% equation %} (X_1\vee Y_1\vee Z_1)\wedge(X_2\vee Y_2\vee Z_2)\wedge\dots\wedge(X_n\vee Y_n\vee Z_n) {% endequation %}

כלומר, הצורה היא זו: "שלשות של משתנים, כשכל המשתנים בשלשה מחוברים על ידי "או", וכל השלשות מחוברות זו עם זו באמצעות "וגם"". העובדה שאלו דווקא <strong>שלשות</strong> של משתנים היא חשובה.

כל שלשה של משתנים שמחוברים ביניהם על ידי "או" נקראת <strong>פסוקית</strong>. המשתנים שבתוך הפסוקיות אינם בהכרח שונים זה מזה - ייתכן שהמשתנה {% equation %}X_2{% endequation %} הוא בדיוק אותו משתנה כמו {% equation %}Z_7{% endequation %} (כלומר - אם מציבים "שקר" במשתנה {% equation %}X_2{% endequation %}, אותו הערך בדיוק יוצב גם ב-{% equation %}Z_7{% endequation %}) וייכתן שאחד המשתנים הוא שלילה של משתנה אחר (כלומר, כשבאחד מהם יוצב "אמת" בשני יוצב "שקר", ולהפך). כפי שנראה בהמשך, זה לא חשוב לצורך ההוכחה.

השאלה המעניינת בהינתן פסוק כזה היא האם הוא <strong>ספיק</strong> או לא - האם קיימת הצבת ערכים למשתנים שעבורה כל הפסוק יקבל את הערך "אמת". מכיוון שכל הפסוקיות מחוברות ביניהן בקשר "וגם", ברור שהפסוק כולו ספיק אך ורק אם קיימת השמה למשתנים שמספקת את כל הפסוקיות בו זמנית.

מתברר שזו <a href="http://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%99%D7%AA_SAT">בעיה קשה מאוד</a>, מבחינה חישובית, לבדוק האם קיימת השמה שכזו. הבעיה העיקרית היא שיש מספר עצום של השמות אפשריות (מה פירוש "מספר עצום" כאן - בפעם אחרת), וייתכן שרק אחת ויחידה מהן מספקת את כל הפסוקיות, ולא ברור האם יש דרך יעילה למצוא אותה שאינה כוללת חיפוש ממצה על כל ההשמות האפשריות (אמרתי קודם שהעובדה שמדובר בשלשות היא חשובה - ואכן, אם כל פסוקית הייתה מורכבת משני משתנים ולא משלושה דווקא הייתה שיטה יעילה למצוא השמה מספקת, אם יש כזו). כמו כן, אין שום הכרח שבאמת תהיה השמה מספקת שכזו.

<strong>אבל</strong>, מה שכן נכון ואני עומד להוכיח, הוא שתמיד יש השמה שמספקת לפחות {% equation %}\frac{7}{8}{% endequation %} מהפסוקיות - כלומר, מספקת "כמעט את כל" הפסוקיות. למעשה, הוכיחו שזה הדבר הכי טוב שמסוגלים לדעת בצורה טריוויאלית - כל בדיקה מסוג "האם יש השמה שמספקת יותר משבע שמיניות מהפסוקיות" היא קשה כמו הבדיקה "האם קיימת השמה שמספקת את כל הפסוקיות".

ההוכחה שלי, כאמור, לא תהיה קונסטרוקטיבית. אני לא אראה שום דרך שבה בונים את ההשמה הזו (אם כי, כאמור, חיפוש ממצה על כל ההשמות ודאי ימצא אותה). המושגים היחידים מתורת ההסתברות שיהיה צורך להכיר לצורך ההוכחה הן "<a href="http://he.wikipedia.org/wiki/%D7%9E%D7%A8%D7%97%D7%91_%D7%9E%D7%93%D7%92%D7%9D">מרחב המדגם</a>", "<a href="http://he.wikipedia.org/wiki/%D7%9E%D7%A9%D7%AA%D7%A0%D7%94_%D7%9E%D7%A7%D7%A8%D7%99">משתנה מקרי</a>" ו"<a href="http://he.wikipedia.org/wiki/%D7%AA%D7%95%D7%97%D7%9C%D7%AA">תוחלת</a>" - מושגים בסיסיים למדי ולא קשים להבנה, אך לרוע מזלי קטונתי מלהציג אותם בעצמי בצורה מסודרת בשלב הזה, ואני מסתמך על ויקיפדיה.

אם עד עכשיו הכל ברור, בפוסט הבא אעבור להוכחה עצמה.
