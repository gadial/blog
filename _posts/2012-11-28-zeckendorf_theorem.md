---
id: 2255
title: "משפט זקנדורף"
date: 2012-11-28 22:53:02
layout: post
categories: 
  - תורת המספרים
tags: 
  - בסיסי ספירה
  - הוכחות
  - מספרי פיבונאצ'י
  - משפט זקנדורף
---
אני רוצה לתת פוסט קליל יחסית הפעם, ולצורך כך בחרתי במשפט שלטעמי הוא חביב ביותר (אם כי אחרים אולי לא יבינו מה אני מוצא בו) שגם יש לו כמה שימושים נחמדים שלא אזכיר כאן ולו ברמז - משפט זקנדורף. כדי להבין מה המשפט אומר, בואו ניזכר בשני מושגים בסיסיים במתמטיקה - בסיסי ספירה, ומספרי פיבונאצ'י.

בסיסי ספירה הם משהו שאנחנו מכירים עוד בבית הספר היסודי: אנחנו יודעים שהמספר שנכתב בתור 142 הוא המאה מאה ארבעים ושתיים, מכיוון שאנו מפרשים אותו באופן הבא: 2 כפול אחד (<strong>ספרת האחדות</strong>) ועוד 4 כפול עשר (<strong>ספרת העשרות</strong>) ועוד 1 כפול מאה (<strong>ספרת המאות</strong>) וכך אנו עושים באופן כללי לכל מספר: אנחנו מחברים את הספרות כשכל ספרה מוכפלת בחזקה כלשהי של 10 (אחד הוא {% equation %}10^{0}{% endequation %}, עשר הוא {% equation %}10^{1}{% endequation %}, מאה הוא {% equation %}10^{2}{% endequation %} וכן הלאה). המספר 10 כאן הוא שרירותי לגמרי; אפשר גם לעבוד עם חזקות של 2 (<strong>בסיס בינארי</strong>) או של 8 (<strong>בסיס אוקטלי</strong>) או של 16 (<strong>בסיס הקסדצימלי</strong> - כאן אנו נזקקים ל-16 ספרות שונות ולכן משתמשים באותיות גדולות מהא"ב הלטיני) וגם כל מספר אחר (נאמר 3, או 7) הוא לגיטימי. המאיה השתמשו בבסיס 20 והבבלים השתמשו בבסיס 60.

אני רוצה הפעם להשתמש בבסיס שונה לגמרי. כזה שבו המקדמים לא מוכפלים רק בחזקות של מספר אחד מסויים, אלא בסדרה "מעניינת" של מספרים. הסדרה הזו תהיה סדרת <strong>מספרי פיבונאצ'י</strong>. הצגתי אותה <a href="http://www.gadial.net/2009/07/01/finding_fibonacci_formula/">כבר בעבר</a>, אבל הנה היא בקצרה שוב: נגדיר {% equation %}F_{0}=0{% endequation %} ו-{% equation %}F_{1}={% endequation %}, וכעת לכל {% equation %}n&gt;1{% endequation %} נגדיר {% equation %}F_{n}=F_{n-1}+F_{n-2}{% endequation %}. נקבל את הסדרה הבאה: {% equation %}0,1,1,2,3,5,8,13,21,\dots{% endequation %}. שני המספרים הראשונים לא הכי רלוונטיים עבורנו (כי מ-0 אי אפשר לקבל מספרים אחרים על ידי כפל, וה-1 בתחילת הסדרה מופיע פעמיים) אז בפוסט הזה אתייחס לסדרה {% equation %}1,2,3,5,8,13,21,\dots{% endequation %}.

סדרת פיבונאצ'י היא מהסדרות המפורסמות במתמטיקה, אם לא המפורסמת שבהן, ומהרבה סיבות מתמטיות אובייקטיביות. אז אם לקחת משהו "מעניין" בתור בסיס ספירה, למה לא לקחת אותם? כמובן, צריך להגביל באופן מסויים את הצורה שבה בונים מהם מספרים; בפרט, צריך להגביל את גודל המקדם שבו כופלים כל אחד מהמספרים. בבסיס עשרוני הגודל המקסימלי של מקדם הוא 9; בבסיס בינארי הוא 1. במה כדאי לבחור? ובכן, אחד מהדברים שאנו מעוניינים בהם כאשר אנו מייצגים מספרים בבסיס מסוים הוא שהייצוג יהיה <strong>יחיד</strong>. אם אותו מספר ניתן לייצוג בכמה דרכים שונות זה עשוי לגרום לבעיות בהוכחות מסויימות שמניחות במובלע יחידות של הייצוג. כעת, אם נרשה אפילו ל-2 להיות מקדם, כבר קל לראות שייצוג יחיד הולך לאיבוד בלא מעט מקרים: למשל, {% equation %}16=2\cdot8=1\cdot3+1\cdot13{% endequation %}, ולכן אם נכתוב את 16 בבסיס פיבונאצ'י נקבל את שתי דרכי הכתיבה {% equation %}100100{% endequation %} ו-{% equation %}20000{% endequation %} (אם לא ברור לכם למה שתי דרכי הכתיבה הללו מייצגות את 16 בבסיס פיבונאצ'י זו הזדמנות טובה לעצור לרגע ולוודא שאתם מבינים את הרעיון בבסיסי ספירה).

אז בואו נגביל את עצמנו רק למקדמים שהם 0 ו-1. במילים אחרות, כל מה שמותר לנו לעשות כדי לקבל מספר מסויים הוא לקחת קבוצה מסויימת של מספרי פיבונאצ'י ולחבר אותם ולקוות שנקבל את המספר שאותו אנו מקווים לקבל. אלא ש<strong>עדיין</strong> אין לנו ייצוג יחיד! למעשה, אם תחשבו שניה תראו שקיימים <strong>המון</strong> מספרים שאין להם ייצוג יחיד. מי הם? מספרי פיבונאצ'י, כמובן... למשל, {% equation %}21{% endequation %} הוא גם {% equation %}1000000{% endequation %} וגם {% equation %}110000{% endequation %}, ותופעה דומה תהיה עבור כל מספר פיבונאצ'י אחר שגדול או שווה ל-3. אז מה עושים? מנסים למצוא עוד הגבלה. אבל איך אפשר להגביל סיטואציות שהן כל כך פשוטות כמו {% equation %}1000000{% endequation %} ו-{% equation %}110000{% endequation %}? ובכן, אולי... אם נאסור על שני 1 להופיע ברצף?

כאן זה נשמע כאילו אני כבר לוקח על עצמי הגבלה גדולה למדי. אני בעצם רוצה להוכיח שאפשר לייצג <strong>כל</strong> מספר טבעי על ידי סכום של מספרי פיבונאצ'י, כך שאין שני מספרים רצופים שנלקחים בסכום, ואני גם רוצה להוכיח כתוספת שהייצוג הזה הוא יחיד. האם זה אפשרי בכלל? באופן מפתיע (עבורי) התשובה היא <strong>כן</strong>! זה בדיוק משפט זקנדורף.

פורמלית, אני רוצה להראות שלכל מספר טבעי {% equation %}n{% endequation %} קיימת ויחידה סדרה {% equation %}a_{2},a_{3},\dots,a_{k}\in\left\{ 0,1\right\} {% endequation %} כך ש-{% equation %}n=\sum_{i=2}^{k}a_{i}F_{i}{% endequation %} (זכרו שהשלכתי מסדרת פיבונאצ'י את שני האיברים הראשונים) ו-{% equation %}a_{i}a_{i+1}=0{% endequation %} לכל {% equation %}2\le i&lt;k{% endequation %} (זו דרך נאה לנסח את הקריטריון של "אין שני מופעים רצופים של 1") ו-{% equation %}a_k=1{% endequation %} (כי אחרת בוודאי שלא יהיה לנו ייצוג יחיד - אפשר להוסיף עוד ועוד אפסים לסוף הסדרה). אם כן, זה המשפט, ועצם זה שהוא נכון הוא מגניב למדי, אבל מטרת הפוסט הזה היא גם להראות לכך הוכחה כלשהי.

נתחיל עם הוכחת הקיום, כלומר שכל מספר טבעי ניתן לייצג בצורה הזו. ההוכחה תהיה, מה לעשות, באינדוקציה על המספר. עבור {% equation %}n=1,2,3{% endequation %} המשפט מובן מאליו כי שלושת אלו הם מספרי פיבונאצ'י. נניח אם כן שלכל מספר קטן מ-{% equation %}n{% endequation %} אנו יודעים למצוא ייצוג זקנדורף ונמצא כזה עבור {% equation %}n{% endequation %} עצמו. מה שמתבקש לעשות הוא להגיד משהו כזה: "יהא {% equation %}F_{k}{% endequation %} מספר פיבונאצ'י הגדול ביותר שעודנו קטן או שווה ל-{% equation %}n{% endequation %}. אם {% equation %}F_{k}=n{% endequation %} סיימנו; אחרת , בואו נסתכל על המספר {% equation %}t=n-F_{k}{% endequation %}. הוא קטן מ-{% equation %}n{% endequation %} אז יש לו ייצוג זקנדורף, ופשוט נוסיף את {% equation %}F_{k}{% endequation %} בסוף שלו". זה כמובן <strong>היה</strong> מסיים את ההוכחה אלמלא החלק המעצבן הזה של לאסור על שני מספרי פיבונאצ'י רצופים בסוף הייצוג, והחלק המעצבן הזה של לאסור על מקדם גדול מ-1. הבעיה הראשונה תתרחש אם {% equation %}F_{k-1}{% endequation %} מופיע בייצוג זקנדורף של {% equation %}t{% endequation %}, והבעיה השניה תתרחש אם {% equation %}F_{k}{% endequation %} עצמו מופיע בייצוג זקנדורף של {% equation %}t{% endequation %}.

שתי הבעיות הללו הן לא בעיות אמיתיות כי אפשר להראות שאם משהו מהן מתרחש, אז {% equation %}F_{k}{% endequation %} הוא לא באמת מספר פיבונאצ'י הגדול ביותר שעדיין קטן מ-{% equation %}n{% endequation %}. כדי לראות זאת, בואו נניח ש-{% equation %}F_{k-1}{% endequation %} או {% equation %}F_{k}{% endequation %} מופיעים בייצוג של {% equation %}t{% endequation %}, כלומר בכל מקרה {% equation %}t\ge F_{k-1}{% endequation %}. מכאן ש-{% equation %}n=t+F_{k}\ge F_{k}+F_{k-1}=F_{k+1}{% endequation %}, דהיינו {% equation %}n{% endequation %} גדול לפחות כמו {% equation %}F_{k+1}{% endequation %}, מה שמסיים את העניין. זה גם מצביע לנו על האלגוריתם שבו אפשר למצוא את ייצוג זקונדורף של מספר: מתחילים ממספר פיבונאצ'י הגדול ביותר שקטן ממנו, מחסרים ואז ממשיכים ברקורסיה. למשל, כדי לייצג את 27 נחסר ממנו את 21, נקבל 6, נחסר ממנו את 5, נקבל 1 והנה קיבלנו את הייצוג {% equation %}1001001{% endequation %} - כפי שאפשר לראות, אין שני מופעים רצופים של 1.

האתגר, אם כן, יהיה להוכיח שייצוג זקנדורף של מספר הוא אכן יחיד - כלומר, שלא נצטרך יותר לחפש <strong>עוד</strong> מגבלות שאפשר להשית על הייצוג. גם את זה נוכיח באינדוקציה. שוב, הבסיס עבור {% equation %}n=1{% endequation %} ברור ולכן ננסה להראות עבור {% equation %}n{% endequation %} כללי שהייצוג שלו יחיד בהינתן שהייצוג של כל מספר שקטן ממנו יחיד.

בואו נשתמש בסימונים הבאים: נכתוב {% equation %}n=a_{1}+a_{2}+\dots+a_{k}{% endequation %} ו-{% equation %}n=b_{1}+b_{2}+\dots+b_{r}{% endequation %} כך שכל ה-{% equation %}a{% endequation %}-ים וה-{% equation %}b{% endequation %}-ים הם מספרי פיבונאצ'י ומסודרים מהקטן לגדול. מטרתנו היא להראות ש-{% equation %}r=k{% endequation %} וש-{% equation %}a_{i}=b_{i}{% endequation %} לכל {% equation %}1\le i\le k{% endequation %}.

ראשית, אם {% equation %}a_{k}=b_{r}{% endequation %} אז סיימנו, כי אפשר פשוט לחסר את המספר המשותף הגדול הזה מ-{% equation %}n{% endequation %} ולהשתמש בהנחת האינדוקציה: נסתכל על המספר {% equation %}n-a_{k}=a_{1}+\dots+a_{k-1}=b_{1}+\dots+b_{r-1}{% endequation %} ומהנחת האינדוקציה נקבל ש-{% equation %}k-1=r-1{% endequation %} וש-{% equation %}a_{i}=b_{i}{% endequation %} לכל {% equation %}1\le i\le k-1{% endequation %}.

אחרת, אנחנו חייבים להגיע לסתירה כלשהי כדי למנוע את האפשרות ששני הייצוגים הם באמת שונים. בואו נניח ש-{% equation %}a_{k}{% endequation %} הוא הגדול מבין שני המספרים {% equation %}a_{k},b_{r}{% endequation %}. מה שאני רוצה לטעון הוא ש-{% equation %}a_{k}{% endequation %} הוא גדול כל כך עד שכל הסכום {% equation %}b_{1}+b_{2}+\dots+b_{r}{% endequation %} לא מסוגל לעבור אותו! כאן אני אהיה חייב מן הסתם להשתמש בכך שבסכום הזה אין שני מספרי פיבונאצ'י סמוכים, אחרת {% equation %}b_{r-1},b_{r}{% endequation %} היו יכולים להיות בדיוק שני המספרים הקודמים ל-{% equation %}a_{k}{% endequation %} בסדרת פיבונאצ'י.

אם כן, הבה ואנסח במפורש את הטענה שמסיימת את ההוכחה: אם {% equation %}A{% endequation %} היא קבוצה של מספרי פיבונאצ'י כך שאין בה שניים סמוכים, ו-{% equation %}F_{k}{% endequation %} הוא מספר פיבונאצ'י הגדול ביותר ב-{% equation %}A{% endequation %}, אז {% equation %}\sum_{F_{i}\in A}F_{i}&lt;F_{k+1}{% endequation %}.

את הטענה הזו נוכיח... ניחשתם, באינדוקציה. במקרה הזה, על {% equation %}k{% endequation %}. כרגיל, עבור {% equation %}k=2{% endequation %} (זה הבסיס כי {% equation %}F_{0},F_{1}{% endequation %} לא במשחק) נקבל את התוצאה באופן טריוויאלי (כי {% equation %}A{% endequation %} חייבת להיות ריקה ולכן סכום איבריה הוא 0). נניח שהטענה נכונה לכל מספר עד {% equation %}F_{k}{% endequation %} ונוכיח עבורו. נתבונן בקבוצה {% equation %}A{% endequation %} כלשהי של מספרי פיבונאצ'י שקטנים מ-{% equation %}F_{k}{% endequation %} כך שאין שניים סמוכים, ולכן בפרט לא ייתכן ש-{% equation %}F_{k-1}{% endequation %} ו-{% equation %}F_{k-2}{% endequation %} נמצאים בקבוצה גם יחד. נניח ש-{% equation %}F_{k-1}{% endequation %} בפנים, אז כל יתר האיברים של {% equation %}A{% endequation %} הם קטנים מ-{% equation %}F_{k-2}{% endequation %}, ולכן על פי הנחת האינדוקציה על {% equation %}F_{k-2}{% endequation %} נקבל שסכום כל יתר איברי {% equation %}A{% endequation %} <strong>קטן</strong> מ-{% equation %}F_{k-2}{% endequation %}, ולכן סכום כל אברי {% equation %}A{% endequation %} <strong>קטן</strong> מ-{% equation %}F_{k-2}+F_{k-1}=F_{k}{% endequation %}. אותם שיקולים מסיימים את ההוכחה גם במקרה שבו דווקא {% equation %}F_{k-2}{% endequation %} בפנים.

סיימנו את הוכחת המשפט. הייתי שמח להראות גם כמה שימושים מגניבים שלו, אבל אני גם לא מכיר יותר מדי כאלו, וגם מה שאני מכיר הוא טכני למדי וחבל יהיה להאריך איתו את הפוסט שמראש ניסה להיות קומפקטי. לכן אני מקווה שאתם מתלהבים מעצם העובדה שקיים למספרים טבעיים ייצוג שכזה על בסיס סדרת פיבונאצ'י - אני בהחלט מתלהב.