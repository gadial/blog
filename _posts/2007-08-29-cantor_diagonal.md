---
id: 52
title: "האלכסון - אסון"
date: 2007-08-29 00:06:01
layout: post
categories: 
  - תורת הקבוצות
---
בפוסט הקודם דיברתי על שיטת האלכסון של קנטור, שבאמצעותה מוכיחים כי המספרים הממשיים אינם בני מניה, וכעת אגש בלי שהיות להוכחה עצמה. כדי לפשט את העניינים לא אוכיח את הטענה על המספרים הממשיים, אלא על תת קבוצה שלהם; בוודאי שאם תת קבוצה של קבוצת הממשיים אינה בת מניה, גם היא עצמה אינה בת מניה (קל להראות התאמה חח"ע מתת הקבוצה לקבוצה שמכילה אותה; נסו למלא את הפרטים). הקבוצה שאבחר היא קבוצת כל המספרים הממשיים שהפיתוח העשרוני שלהם הוא מהצורה {% equation %}0.a_1a_2a_3\dots{% endequation %}, כאשר {% equation %}a_k{% endequation %}, לכל {% equation %}k{% endequation %} טבעי, הוא או הספרה 0 או הספרה 1.

למה להגביל את עצמי לספרות 0 ו-1? כדי להימנע לחלוטין מכל סכנה של גלישה לשאלות של ייצוג. לפיתוח עשרוני (וגם בשאר בסיסי הספירה) התכונה ה"מוזרה" שקיימים מספרים שניתן לכתוב בשתי דרכים שונות - המקרה המפורסם ביותר הוא זה של {% equation %}1{% endequation %} ו-{% equation %}0.999\dots{% endequation %}, שראוי לפוסט משל עצמו. הימנעות משימוש בספרה 9 מונעת כל בלבול שכזה.

כדי לעשות חיים עוד יותר קלים, אפסיק לדבר על פיתוח עשרוני ואדבר על סדרות; כל איבר בקבוצה שאני עוסק בה הוא בעצם סדרה אינסופית של ספרות שהן 0 או 1 - הסדרה {% equation %}a_1,a_2,a_3,\dots{% endequation %}. מספיק להראות כי מספר הסדרות הללו אינו בן מניה.

ההוכחה היא כדלהלן. נניח בשלילה שמספר הסדרות הוא דווקא כן בן מניה, אז קיימת התאמה חח"ע ועל בין הסדרות למספרים הטבעיים - כלומר, לכל סדרה אפשר להתאים באופן חח"ע מספר טבעי. אם כן, אפשר לסדר את הסדרות במעין טבלה, שבכל שורה יש סדרה: בשורה מספר 3 תהיה סדרה מספר שלוש, וכן הלאה. כל עמודה בטבלה תייצג איבר בסדרה: בעמודה 2 יהיה האיבר השני בסדרה, וכן הלאה.

כעת מגיע הטוויסט. אנו מסתכלים ב<strong>אלכסון</strong> של הטבלה הזו - כלומר, באיבר הראשון בסדרה הראשונה, באיבר השני בסדרה השניה, וכן הלאה. האלכסון הזה הוא בעצמו סדרה אינסופית. כעת ניקח את הסדרה ה"הפוכה" לאלכסון - כלומר, אם האיבר הראשון באלכסון היה 1, האיבר הראשון בסדרה ההפוכה יהיה 0, וכן הלאה.

מה קיבלנו? עוד סדרה אינסופית של אפסים ואחדים. כלומר, היא איבר בקבוצה שלנו, ולכן הותאם לה מספר טבעי כלשהו, ולכן היא מופיעה בטבלה במקום כלשהו. אבל היכן?

לא ייתכן שהיא תופיע במקום הראשון; הרי הספרה הראשונה בה בבירור שונה מהספרה הראשונה של הסדרה שבמקום הראשון (כי הספרה הזו הופיעה באלכסון, ולקחנו את "ההפך" שלה). ומה באשר למקום השני? הפעם אין בעיה עם הספרה הראשונה בסדרה שלנו, אבל יש בעיה עם הספרה <strong>השניה</strong> - הרי הספרה השניה בסדרה השניה נמצאת באלכסון, ולכן היא שונה מזו שסדרה שלנו. וכן הלאה וכן הלאה. לא משנה באיזו שורה נבחר - תהיה בה עמודה שנכנסה לאלכסון, ולכן הסדרה שלנו שונה מהסדרה שבאותה שורה בעמודה הזו. האלכסון מוודא שהסדרה שלנו תהיה שונה מכל סדרה שמופיעה בטבלה. המסקנה? הסדרה שלנו לא מופיעה בטבלה. סתירה.

(בכיוון האחר, ברור שלכל מספר טבעי אפשר להתאים סדרה כלשהי של 0 ו-1: המספר כשהוא מוצג בבסיס בינארי).

כאמור בפוסט הקודם, קנטור עצמו השתמש בהוכחה הזו כדי לתת דוגמה לשימוש במשפט אחר שלו - משפט שעוסק במספרים טרנסצנדנטיים (מושג שהזכרתי באחד הפוסטים הישנים שלי, על בניית המספרים). כדי להסביר מהו מספר טרנסצנדנטי קל יותר להסביר מהו מספר אלגברי: מספר אלגברי הוא מספר שהוא פתרון של משוואה פולינומית שמקדמיה רציונליים. למשל, שורש 2 הוא הפתרון של המשוואה {% equation %}x^2-2=0{% endequation %}. מספר טרנסצנדנטי הוא מספר ממשי שאינו אלגברי. שני המספרים הטרנסצנדנטיים הידועים ביותר הם הקבועים {% equation %}e{% endequation %} ו-{% equation %}\pi{% endequation %}, אבל ההוכחה לטרנסצנדנטיות שלהם אינה פשוטה (של {% equation %}e{% endequation %} קלה יותר מאשר של {% equation %}\pi{% endequation %}, אך בשני המקרים ההוכחה מסובכת יחסית). יש מספרים אחרים, שקל יותר להוכיח את הטרנסצנדנטיות שלהם, והמתמטיקאי ז'וזף ליוביל הציג כאלו (שנבנו במיוחד בשביל להראות את קיומם של מספרים טרנסצנדטיים) -"<a href="http://en.wikipedia.org/wiki/Liouville_number">מספרי ליוביל</a>". בכל המקרים הללו נדרשת כמות לא מועטה של עבודה.

והנה, ההוכחה של קנטור מראה כמעט מייד ש<strong>רוב</strong> המספרים הממשיים הם טרנסצנדנטיים! זוהי ה"דוגמה" המובטחת, והיא נובעת מכך שקנטור הוכיח באותו מאמר שבו הופיעה שיטת האלכסון גם שישנו רק מספר בן מניה של מספרים אלגבריים. הסיבה לכך, בנפנוף ידיים מהיר, היא שכל מספר אלגברי מוגדר באמצעות משוואה אחת לפחות, וכל משוואה מוגדרת באופן מוחלט באמצעות מקדמיה - כך שיש התאמה חח"ע ועל בין סדרות סופיות של רציונליים ובין המשוואות שמגדירות מספרים אלגבריים. עוד צריך להראות שיש מספר בן מניה של סדרות סופיות שאבריהן בני מניה, ויש עוד נקודות עדינות להתייחס אליהן, אבל נראה לי שהרעיון ברור.

אם כן, יש רק מספר בן מניה של מספרים אלגבריים, ויש מספר לא בן מניה של מספרים ממשיים - ולכן יש מספר לא בן מניה של מספרים טרנסצנדנטיים. עד כדי כך פשוט.

אבל כעת חוזרת אלינו הטענה המקורית שלי, לפיה את רוב המספרים הממשיים אי אפשר לחשב, וכעת ההוכחה היא טריוויאלית: יש מספר לא בן מניה של ממשיים, אבל רק מספר בן מניה של תוכניות מחשב בשפה ++C. גמרנו.

נשאר רק להבין למה יש רק מספר בן מניה של תוכניות מחשב שכאלו. ובכן, כל תוכנית היא רצף של תווי ASCII. יש מספר סופי של תווים כאלו (מצדי שיהיה אפילו בן מניה). על כל תוכנית מחשב אפשר לחשוב בתור סדרה של תווים. לפני שניה טענתי (בנפנוף ידיים, אני מודה - אבל ההוכחה הטכנית אינה מסובכת) שיש רק מספר בן מניה של סדרות סופיות שאבריהן שייכים לקבוצה בת מניה. זהו. דרך אחרת לחשוב על זה שמתבססת על סופיות קבוצת תווי ה-ASCII היא לחשוב על תוכנית מחשב כעל <strong>מספר</strong> בייצוג בבסיס שגודלו כגודל קבוצת תווי ה-ASCII הקיימים; התו הראשון בתוכנית הוא ספרת ה"אחדות", התו השני הוא ספרת ה"עשרות", וכן הלאה. כך מתאימים באופן חח"ע ועל מספר לכל תוכנית.

כך, בצורה אגבית למדי, ראינו שקיימים דברים שלעולם לא נוכל לחשב. הטענה הזו נשמעת נחרצת למדי - בסך הכל דיברתי על תוכניות בשפת ++C, אולי בשפה חזקה יותר (Ruby!) כן אפשר לחשב? אבל כפי שכבר אמרתי קודם, ++C היא מה שמכונה Turing Complete; לא משנה באיזה מחשב (אפילו קוואנטי) ובאיזה שפת תכנות נבחר - ניתן יהיה לכתוב תוכנית ++C שעושה את אותו הדבר בדיוק.

לטעמי ההוכחה הזו היא עלובה ולא מספקת. היא אמנם אומרת שיש המון מספרים קשים לחישוב, אבל לא אומרת כלום על מה הם. זו הוכחה לא קונסטרוקטיבית "מעצבנת", כי היא מוכיחה אי היתכנות;  מצד אחד היא חורצת לשון ואומרת "אי אפשר ואי אפשר!" ומצד שני לא אומרת מה אי אפשר. אני מעדיף הוכחות שאומרות "אפשר" ולא מראות איך.

זו כנראה הסיבה שבגללה מעדיפים להציג בכל דיון במגבלות יכולתו של המחשב את "<a href="http://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%99%D7%AA_%D7%94%D7%A2%D7%A6%D7%99%D7%A8%D7%94">בעיית העצירה</a>" המפורסמת, שמצביעה על חוסר יכולת מאוד קונקרטי ומרכזי של המחשב, ומהווה בסיס להוכחת אי היכולת לפתור המוני בעיות קונקרטיות אחרות. אני מקווה להרחיב בנושא באחד מהפוסטים הבאים.
