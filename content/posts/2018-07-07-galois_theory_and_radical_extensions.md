---
id: 3635
title: "תורת גלואה ופתרון משוואות באמצעות רדיקלים"
date: 2018-07-07 21:01:05
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - פתרון משוואות באמצעות רדיקלים
  - תורת גלואה
---
<h2>מבוא</h2>
בסדרת הפוסטים הנוכחית הצגתי את הבסיס של תורת גלואה: ראינו את המשפט היסודי שמקשר בין המבנה של הרחבת שדות והמבנה של חבורת האוטומורפיזמים של ההרחבה, וראינו כמה שימושים של התורה הזו כדי להבין יותר טוב איך עובדות הרחבות של שדות. מה שלא ראינו עדיין הוא את הפואנטה - הסיבה שבגללה גלואה המציא מלכתחילה את כל זה: מה שנקרא <strong>פתרון משוואות פולינומיות באמצעות רדיקלים</strong>.

הנושא הזה הוא אחד מהשיאים בכל תיאור היסטורי של התפתחות המתמטיקה, כי זוהי הבעיה שהפכה את האלגברה הקלאסית למה שאנחנו קוראים לו היום "אלגברה מודרנית". מה שגלואה עשה היה אחד מהבסיסים המרכזיים להמצאת המושגים של <strong>חבורה</strong> ושל <strong>שדה</strong>, ומרתק להיכנס לפרטים המלאים של הנושא. רק שלא אעשה את זה כרגע אלא כנראה במועד מאוחר יותר, כי בהיסטוריה של המתמטיקה אני חושב שצריך קודם להבין טוב את ה"איך" לפני שמדברים על ה"מה ולמה".

בואו נתחיל עם הדוגמא המנחה שנותנת מוטיבציה לכל הסיפור הזה - הנוסחה לפתרון משוואה ריבועית. <strong>משוואה ריבועית</strong> היא ביטוי מהצורה {% equation %}ax^{2}+bx+c=0{% endequation %} כאשר {% equation %}x{% endequation %} הוא <strong>משתנה</strong> ואילו ה-{% equation %}a,b,c{% endequation %} הם <strong>מקדמים</strong> מספריים. <strong>פתרון</strong> של משוואה ריבועית הוא מספר {% equation %}\theta{% endequation %} שאפשר להציב במקום {% equation %}x{% endequation %}, לבצע את החישוב {% equation %}a\theta^{2}+b\theta+c{% endequation %} ולבדוק אם קיבלנו אפס או לא (בלשון של הפוסטים האחרונים - נתון לנו<strong> פולינום</strong> ממעלה שניה ואנחנו רוצים למצוא שורש שלו). מה שאנחנו באמת רוצים הוא <strong>נוסחה</strong> שנותנת לנו פתרונות של משוואה שכזו בלי שנצטרך להתאמץ, ובתיכון לומדים שהקסם הזה הוא אפשרי, במחיר אחת הנוסחאות המזעזעות ביותר שהציבור הרחב נחשף להן, ואחת מהיחידות שאני זוכר בעל פה עד היום:

{% equation %}x_{1,2}=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}{% endequation %}

איך בכלל הגיעו לנוסחה מפלצתית שכזו? <a href="https://gadial.net/2008/01/26/solving_quadratic_equations/">אחד מהפוסטים החביבים עלי</a> בבלוג עוסק בדיוק בשאלה הזו. ברשותכם, אני רוצה לענות עליה שוב, אבל בצורה קצת שונה ויותר מתוחכמת, שתתאים למה שאני הולך לעשות בהמשך. ראשית, ההנחה הבסיסית שלי היא שאותם {% equation %}a,b,c{% endequation %} וגם {% equation %}\theta{% endequation %} נלקחים כולם מתוך <strong>שדה</strong>. כלומר, שאפשר לחבר, לכפול, לחסר <strong>ולחלק</strong> אותם. אפשר גם לדבר על פתרון משוואות מעל חוג, שהוא מקרה יותר כללי, אבל שם לא תמיד יהיו פתרונות וזה נושא לדיון נפרד; עדיף קודם כל להבין את המקרה הפשוט. כמו כן, הנחה נוספת שלי היא ש-{% equation %}a\ne0{% endequation %} אחרת יש לנו ביד משוואה אחרת, פשוטה יותר: {% equation %}bx+c=0{% endequation %}. אם גם {% equation %}b=0{% endequation %} אז הפכנו למשוואה {% equation %}c=0{% endequation %} שהיא או נכונה או לא; אין לה "פתרונות" ספציפיים. אם {% equation %}b\ne0{% endequation %} אז אפשר לחלק בו ולקבל {% equation %}x=-\frac{c}{b}{% endequation %}, כלומר זה מקרה קל עם פתרון יחיד. לכן המקרה המעניין הראשון הוא {% equation %}ax^{2}+bx+c{% endequation %} עם ההנחה הנוספת {% equation %}a\ne0{% endequation %}.

אם {% equation %}a\ne0{% endequation %} אפשר <strong>לפשט</strong> את המשוואה על ידי חלוקה בו: נקבל את המשוואה {% equation %}x^{2}+\frac{b}{a}x+\frac{c}{a}{% endequation %}. בואו נסמן {% equation %}A=\frac{b}{x}{% endequation %} ו-{% equation %}B=\frac{c}{a}{% endequation %} ונקבל את המשוואה הפשוטה יותר {% equation %}x^{2}+Ax+B=0{% endequation %}. המפתח לפתרון המשוואה הזו טמון ב<strong>עוד</strong> תעלול, שנקרא "השלמה לריבוע" ואפשר לתאר בדרך ציורית ויפה ועשיתי את זה בפוסט ההוא, אבל בואו פשוט נציג אותו כאן בדרך שנוחה לי: אני מבצע <strong>החלפת משתנה</strong> על ידי הגדרת {% equation %}y=x+\frac{A}{2}{% endequation %}. חשוב לי שנראה את ההצבה הזו כי ההתמודדות עם משוואות ממעלה שלישית ורביעית מתחילה באותו האופן. מההצבה הזו אנחנו מקבלים

{% equation %}x=y-\frac{A}{2}{% endequation %}

ולכן גם

{% equation %}x^{2}=y^{2}-Ay+\frac{A^{2}}{4}{% endequation %}

ואחרי שנציב את זה במשוואה המקורית, נקבל

{% equation %}x^{2}+Ax+B=\left(y^{2}-Ay+\frac{A^{2}}{4}\right)+A\left(y-\frac{A}{2}\right)+B={% endequation %}

{% equation %}=y^{2}+\frac{A^{2}-2A^{2}+4B}{4}=y^{2}+\frac{-A^{2}+4B}{4}=y^{2}-\frac{A^{2}-4B}{4}{% endequation %}

עכשיו אפשר להעביר את הביטוי הימני אגף, ולקבל:

{% equation %}y^{2}=\frac{A^{2}-4B}{4}{% endequation %}

ועכשיו מגיע פתאום מהלך חדש, ששובר את כללי המשחק: אנחנו <strong>מוציאים שורש ריבועי</strong> ומקבלים {% equation %}y_{1,2}=\pm\frac{\sqrt{A^{2}-4B}}{2}{% endequation %}. השאלה "האם בכלל מותר לנו להוציא פה שורש?" היא מצויינת ועוד מעט נחזור אליה.

עכשיו, משיש לנו פתרון למשוואה עם {% equation %}y{% endequation %}, אפשר לחזור ממנו אל פתרון למשוואה עם {% equation %}x{% endequation %}:

{% equation %}x_{1,2}+\frac{A}{2}=\pm\frac{\sqrt{A^{2}-4B}}{2}{% endequation %}

{% equation %}x_{1,2}=\frac{-A\pm\sqrt{A^{2}-4B}}{2}{% endequation %}

ועכשיו אפשר לחזור למשוואה עם {% equation %}a,b,c{% endequation %}:

{% equation %}x_{1,2}=\frac{-\frac{b}{a}\pm\sqrt{\frac{b^{2}}{a^{2}}-4\frac{c}{a}}}{2}=\frac{a}{a}\frac{-\frac{b}{a}\pm\sqrt{\frac{b^{2}}{a^{2}}-4\frac{c}{a}}}{2}={% endequation %}

{% equation %}=\frac{-a\cdot\frac{b}{a}\pm\sqrt{a^{2}\cdot\left(\frac{b^{2}}{a^{2}}-4\frac{c}{a}\right)}}{2a}=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}{% endequation %}

זה מסיים את הסיפור של המשוואה ממעלה שניה, אבל בואו נראה מה הדברים שלמדנו מפה:
<ol>
 	<li>ה"עולם" שבו כל הסיפור הזה מתרחש הוא <strong>שדה</strong> {% equation %}F{% endequation %} כלשהו.</li>
 	<li>בעולם הזה אנחנו מקבלים פולינום {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} ומחפשים שורש שלו (או אפילו טוב יותר, את כל השורשים בבת אחת אם אפשר)</li>
 	<li>הנוסחה שלנו נותנת לנו <strong>אלגוריתם</strong> שבונה את שורשי המשוואה באמצעות מספר <strong>סופי</strong> של פעולות.</li>
 	<li>הפעולות שבהן מותר לנו להשתמש הן: חיבור, חיסור, כפל, חילוק <strong>והוצאת שורש</strong>.</li>
 	<li>הקלטים האפשריים של האלגוריתם הם האיברים של {% equation %}F{% endequation %}. בפרט, <strong>המקדמים</strong> של הפולינום {% equation %}p\left(x\right){% endequation %} יכולים להיות חלק מהקלט.</li>
</ol>
דבר אחד ויחיד שלא הופיע בדוגמא הזו במפורש, וכן יופיע אם ננסה לפתור משוואה ממעלה שלישית הוא ש"הוצאת שורש" כאן אין פירושה רק "הוצאת שורש <strong>ריבועי</strong>" אלא הוצאה של שורש מכל סדר סופי, מה שאנחנו מסמנים בתור הפעולה {% equation %}\sqrt[n]{a}{% endequation %}.

אני אתן הגדרה פורמלית יותר בהמשך, אבל הנה רוח הדברים: אנחנו אומרים שפולינום {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} ניתן ל<strong>פתרון באמצעות רדיקלים</strong> אם יש נוסחה שעונה לתנאים למעלה עבור השורשים שלו. כעת אפשר לחזור לרגע לסיפור ההיסטורי: נוסחת השורשים עבור משוואה ממעלה שניה הייתה ידועה לאנושות עוד משחר ההיסטוריה; למשל, אצל הבבלים יש לה תיאורים מפורשים. צריך קצת להיזהר עם הניסוח האנכרוניסטי של הטענה הזו, כי המושג של <strong>נוסחה</strong> בכלל לא היה קיים אצל הבבלים, והם לא טיפלו בכל המקרים האפשריים של נוסחת השורשים; אבל מה שהיה להם הוא, בשורה התחתונה, אלגוריתם כדוגמת זה שתיארתי פה.

לעומת זאת, נוסחאות לפתרון באמצעות רדיקלים של משוואות ממעלה שלישית ורביעית זה עניין חדש הרבה יותר, שמקורו באיטליה של תקופת הרנסנס. הסיפור של הגילוי שלהן הוא אחד מהמרתקים בכל תולדות המתמטיקה, בגלל התחרות הקשה שהייתה מעורבת בכך, והאופן שבו המספרים המרוכבים צצו לראשונה מתוכו באופן בלתי נמנע בעליל (ועוד אחזור לזה כשאדבר על פתרון משוואות ממעלה שלישית). החיפוש אחר נוסחה כללית לפתרון משוואה ממעלה <strong>חמישית</strong> הפך מאז אותה תקופה לאחד מהנושאים הלוהטים ביותר במתמטיקה, עד שבשנת 1824 המתמטיקאי נילס הנריק אבל הוכיח (תוך היעזרות בתוצאה חלקית של פאולו רופיני מ-1799) שזה פשוט בלתי אפשרי: אין נוסחה כללית לפתרון באמצעות רדיקלים של משוואה ממעלה חמישית ומעלה. גם אחרי שאבל פרסם את ההוכחה שלו, עדיין נותרה פתוחה שאלה מהותית לא פחות - מתי <strong>כן</strong> אפשר לפתור משוואות ממעלה חמישית ומעלה באמצעות רדיקלים? אבל לא הספיק לפתור את השאלה הזו כי נפטר ב-1829 ממחלה, כשהוא רק בן 26. מי שכן פתר את השאלה הזו היה אווריסט גלואה, שחייו היו טראגיים אף יותר; הוא נהרג בדו-קרב ב-1832 כשהוא בן 20 בלבד, אבל התורה המתמטית שהשאיר אחריו (והראשון ש"פיענח" ופרסם היה ליוביל, ב-1846) הפכה להיות אחד מאבני היסוד באלגברה המודרנית, ובפרט ענתה באופן מלא על האתגר: היא סיפקה תנאי הכרחי ומספיק לכך שמשוואה <strong>כלשהי</strong> תהיה ניתנת לפתרון באמצעות רדיקלים. את התנאי ניתן לנסח בפשטות: לכל משוואה אפשר להתאים <strong>חבורה</strong> - חבורת גלואה של המשוואה הזו, והמשוואה היא פתירה אם ורק אם החבורה היא... אה... פתירה?

בניסוח הזה לא ברור מה בעצם גלואה עשה, עד שאנחנו נזכרים שכל המהות של תורת גלואה היא <strong>רדוקציה</strong>: רדוקציה של שאלות קשות על שדות לשאלות קלות יותר על חבורות. המושג של "חבורה פתירה", <a href="https://gadial.net/2017/08/10/commutators_and_solvable_groups/">שהצגתי לקראת סוף סדרת הפוסטים שלי</a> על תורת החבורות, הוא פשוט יחסית. בפרט קל יחסית להראות שהחבורה שמייצגת את המשוואה הכללית ממעלה חמישית היא לא פתירה. מיותר לציין שהשם "חבורה פתירה" הגיע בדיוק מהמקום הזה; "חבורה פתירה" פירושו "חבורה שהיא חבורת גלואה של משוואה פולינומית שפתירה על ידי רדיקלים".

המשך הסיפור כולל כמה עניינים עיקריים: ראשית, צריך לראות את התוצאה הכללית של גלואה שבה, בהינתן פולינום קונקרטי, הפתירות של הפולינום מומרת בפתירות של חבורה. בשביל זה נצטרך גם להזכיר לעצמנו את המושג של חבורה פתירה ולהוכיח עליהן דברים שלא הוכחתי עד כה בבלוג. שנית, צריך להבין את העניין הקצת חמקמק הזה של "משוואה כללית", שתורת גלואה לכאורה לא מטפלת בה אבל עם עוד קצת עבודה טכנית נראה שהיא כן. לבסוף צריך להסביר למה החבורה הספציפית שמתאימה למשוואה הכללית ממעלה 5 ומעלה היא לא פתירה ואילו עבור מעלות 1,2,3,4 היא כן פתירה; זו עוד הוכחה שהתחמקתי ממנה בבלוג עד כה ולא אתחמק ממנה עתה.
<h2>מה הרעיון הכללי מאחורי ההוכחה של גלואה?</h2>
אם {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %} הוא פולינום ספרבילי אז שדה הפיצול שלו (כלומר, מה שמתקבל מ-{% equation %}F{% endequation %} על ידי הוספת שורשי הפולינום הזה) הוא הרחבת גלואה ואפשר לדבר על חבורת הגלואה שלה; לחבורת הגלואה הזו גם קוראים בשם חבורת הגלואה של הפולינום {% equation %}p{% endequation %} מעל {% equation %}F{% endequation %}. במקרים הנפוצים שמעניינים אותנו שבהם {% equation %}F{% endequation %} הוא שדה ממציין 0 או שדה סופי, אין צורך לדרוש ש-{% equation %}p\left(x\right){% endequation %} יהיה ספרבילי; שדה הפיצול שלו עדיין יהיה גלואה, ולכן מעכשיו אדבר בחופשיות על חבורת הגלואה של כל פולינום (רק צריך לזכור שאם עובדים מעל שדה אינסופי שאינו מושלם צריך להיות זהירים מאוד). מה שאיברים בחבורה הזו עושים הוא לבצע <strong>פרמוטציות</strong> על שורשים של הפולינום הזה; למעשה, זו הייתה נקודת המוצא של גלואה. הוא לא דיבר על חבורות באופן כללי אלא על אוספי הפרמוטציות של פתרונות של משוואות, כאשר הפרמוטציות הללו גם "משחקות יפה" עם השדה (כלומר, הן <strong>אוטומורפיזם</strong>).

עכשיו נדבר על מה זה אומר לפתור על ידי רדיקלים. נניח ש-{% equation %}E/F{% endequation %} היא הרחבת שדות כלשהי ו-{% equation %}a\in E{% endequation %}. נאמר ש-{% equation %}a{% endequation %} ניתן להבעה בעזרת רדיקלים אם קיימת סדרה של שדות,

{% equation %}F=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=E{% endequation %} כך שלכל {% equation %}0\le i&lt;n{% endequation %} מתקיים ש-{% equation %}E_{i+1}=E_{i}\left(\sqrt[k_{i}]{a_{i}}\right){% endequation %} עבור {% equation %}k_{i}\ge2{% endequation %} טבעי ו-{% equation %}a_{i}\in E_{i}{% endequation %} כלשהו (עוד אסביר בהמשך מה זה בדיוק שורש שכזה). הרחבה כזו של שדה, שמתקבלת מהוספה של שורש {% equation %}k{% endequation %}-י של איבר בשדה, נקראת <strong>הרחבה רדיקלית פרימיטיבית</strong>; ואם יש לנו מגדל כזה של הרחבת שדות שבו כל צעד הוא הרחבה רדיקלית פרימיטיבית, אז כל העסק נקרא <strong>הרחבה רדיקלית</strong>; ואם יש לנו פולינום מעל שדה הבסיס אומרים שהוא <strong>ניתן לפתרון באמצעות רדיקלים</strong> אם כל השורשים שלו נמצאים בהרחבות רדיקליות של שדה הבסיס.

ההגדרה הזו מזכירה מאוד את מה שראינו לגבי בעיות בניה בסרגל ומחוגה; מספר {% equation %}a\in\mathbb{R}{% endequation %} כלשהו הוא ניתן לבניה בסרגל ומחוגה אם ורק אם קיימת סדרה של שדות, {% equation %}\mathbb{Q}=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=F\left(a\right){% endequation %} כך ש-{% equation %}\left[E_{i+1}:E_{i}\right]=2{% endequation %}. למרות הדמיון, חשוב גם לשים לב להבדל: ראשית, אם {% equation %}E_{i+1}=E_{i}\left(\sqrt[k_{i}]{a_{i}}\right){% endequation %} אז בהחלט ייתכן ש-{% equation %}\left[E_{i+1}:E_{i}\right]{% endequation %} יהיה גדול מ-2 (הגודל חסום על ידי {% equation %}k_{i}{% endequation %}). מצד שני, {% equation %}\left[E_{i+1}:E_{i}\right]=2{% endequation %} זה קצת פחות אינפורמטיבי לגבי איך בדיוק {% equation %}E_{i+1}{% endequation %} מתקבל מ-{% equation %}E_{i}{% endequation %}. אנחנו יודעים שבמקרה הזה, {% equation %}E_{i+1}{% endequation %} התקבל על ידי הוספת שורש של פולינום ממעלה שניה, אבל שורש של פולינום זה לא אותו דבר כמו הפעולה "הוצאת שורש". דוגמא קלאסית לכך היא המספר {% equation %}\varphi=1.61803\dots{% endequation %} המכונה "יחס הזהב"; הוא שורש של הפולינום {% equation %}x^{2}-x-1{% endequation %} מעל {% equation %}\mathbb{Q}{% endequation %}, אבל <strong>לא קיים</strong> מספר רציונלי {% equation %}a\in\mathbb{Q}{% endequation %} כך ש-{% equation %}\varphi=\sqrt[k]{a}{% endequation %}, לכל {% equation %}k{% endequation %}. במילים אחרות, לא כל הרחבה ממימד 2 היא הרחבה רדיקלית פרימיטיבית, ובואו לא נדבר אפילו על ממדים גבוהים יותר.

אז מצד אחד, העובדה שאנחנו לא יכולים להגיד שום דבר על {% equation %}\left[E_{i+1}:E_{i}\right]{% endequation %} מונעת מאיתנו להשתמש בטכניקות הסופר-פשוטות שהראו שאי אפשר לחלק זוויות לשלוש או להכפיל את הקוביה. מצד שני, העובדה שאנחנו כן יודעים משהו מהותי על האופן שבו {% equation %}E_{i+1}/E_{i}{% endequation %} נוצרת מאפשר לנו להגיד משהו מהותי על חבורת הגלואה שמתאימה לה, וזה המפתח לסיפור כולו.

בנפנוף ידיים פרוע, הרעיון הוא שאם יש לנו הרחבה רדיקלית פרימיטיבית, ואם השדה שמעליו אנחנו עובדים הוא "נחמד מספיק", אז חבורת הגלואה של ההרחבה הזו תהיה <strong>ציקלית</strong>. ה"נחמד מספיק" פשוט אומר כאן "כולל את כל שורשי היחידה מסדר כך וכך" ונדבר על זה במפורט בהמשך. הנקודה היא ששורשי יחידה הם בעצמם, ובכן, שורשים; ולכן אפשר תמיד, כשבונים הרחבה רדיקלית, להוסיף אותם "על הדרך".

כשטיפלתי בבעיית הבניה של מצולע משוכלל, הסיטואציה הייתה שהייתה לנו סדרה של הרחבות:

{% equation %}E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{k}{% endequation %}

שהתאימו לסדרה של חבורות:

{% equation %}G_{k}\subseteq G_{k-1}\subseteq G_{k-2}\subseteq\dots\subseteq G_{0}{% endequation %}

והרעיון היה שמתקיים {% equation %}\text{Gal}\left(E_{i+1}/E_{i}\right)\cong G_{i}/G_{i+1}{% endequation %} (אני אוכיח את זה בהמשך למקרה שזה לא ברור). לכן, אם יש לנו הרחבה רדיקלית שמקיימת את המה-שזה-לא-יהיה עם שורשי היחידה, אנחנו נקבל שחבורת הגלואה שלה כוללת סדרה עולה של תתי-חבורות (החל מהטריוויאלית ועד לחבורה כולה) כך שהמנה של כל שתי חבורות עוקבות היא ציקלית. לחבורה שמקיימת את התכונה הזו יש שם: <strong>חבורה פתירה</strong>. ליתר דיוק, ההגדרה שהראיתי עד כה לחבורות פתירות הייתה קצת שונה, אבל כאשר החבורה היא <strong>סופית</strong> אז היא פתירה אם ורק אם קיימת בה סדרת תתי-חבורות שכזו - את זה אני אוכיח בפוסט המשך שיתעסק כולו בחומר של תורת החבורות שרלוונטי לעניין הזה שלנו ועדיין לא הראיתי בבלוג.
<h2>הרחבות רדיקליות פרימיטיביות</h2>
בואו ננסה להבין עכשיו איך "עובדת" הרחבה רדיקלית פרימיטיבית. זו הרחבה {% equation %}E/F{% endequation %} כך שמתקיים {% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} עבור {% equation %}a\in F{% endequation %} ו-{% equation %}n\ge2{% endequation %} כלשהו, אבל מה המשמעות של {% equation %}\sqrt[n]{a}{% endequation %} בכלל? זה ביטוי שהוא <strong>לא מוגדר היטב</strong> כי לכל {% equation %}a\in F{% endequation %} השונה מאפס קיימים {% equation %}n{% endequation %} שורשים <strong>שונים</strong> בשדה הפיצול של הפולינום {% equation %}x^{n}-a{% endequation %} למעט במקרה שבו {% equation %}F{% endequation %} הוא ממציין שמחלק את {% equation %}n{% endequation %} - ועל מקרה כזה לא נדבר פה. בכל מקרה אחר, הנגזרת של {% equation %}x^{n}-a{% endequation %} היא פשוט {% equation %}nx^{n-1}{% endequation %} שזר ל-{% equation %}x^{n}-a{% endequation %} (למשל, כי השורש היחיד של {% equation %}nx^{n-1}{% endequation %} הוא 0, שאיננו שורש של {% equation %}x^{n}-a{% endequation %}) ולכן {% equation %}x^{n}-a{% endequation %} הוא <strong>פולינום ספרבילי</strong>, כלומר יש לו {% equation %}n{% endequation %} שורשים שונים. אבל מי הם?

ובכן, ברור ש-0 אינו שורש. אם {% equation %}\alpha,\beta{% endequation %} הם שניהם שורשים, אז {% equation %}\alpha^{n}=\beta^{n}=a{% endequation %} ולכן {% equation %}\left(\frac{\alpha}{\beta}\right)^{n}=1{% endequation %}, מה שאומר ש-{% equation %}\frac{\alpha}{\beta}{% endequation %} הוא <strong>שורש יחידה</strong> מסדר {% equation %}n{% endequation %}. כרגיל, אני אסמן ב-{% equation %}\omega_{n}\triangleq e^{\frac{2\pi i}{n}}{% endequation %} את אחד משורשי היחידה הפרימיטיביים מסדר {% equation %}n{% endequation %}, ואז <strong>כל</strong> שורש יחידה מסדר {% equation %}n{% endequation %} הוא מהצורה {% equation %}\omega_{n}^{k}{% endequation %}, כך שאפשר לכתוב {% equation %}\beta=\alpha\omega_{n}^{k}{% endequation %}. יותר מכך: אם {% equation %}\omega_{n}^{k}{% endequation %} הוא שורש יחידה מסדר {% equation %}n{% endequation %} כלשהו, אז {% equation %}\left(\alpha\omega_{n}^{k}\right)^{n}=\alpha^{n}\cdot1=a{% endequation %}. המסקנה: אם ניקח שורש <strong>כלשהו</strong> של {% equation %}x^{n}-a{% endequation %}, לא משנה בכלל איזה, אז <strong>כל</strong> שורש של הפולינום מתקבל מהכפלה שלו בשורש יחידה פרימיטיבי, וכל הכפלה שלו בשורש יחידה פרימיטיבי נותנת שורש של הפולינום. המסקנה היא שאפשר לסמן ב-{% equation %}\sqrt[n]{a}{% endequation %} את אחד מהשורשים של {% equation %}x^{n}-a{% endequation %} באופן <strong>שרירותי לגמרי</strong> - לא משנה איזה שורש נבחר - ואז נקבל שכל השורשים של הפולינום הם בדיוק {% equation %}\omega_{n}^{k}\sqrt[n]{a}{% endequation %} עבור {% equation %}0\le k&lt;n{% endequation %}.

הדוגמא הפשוטה ביותר היא זו של שורשים "רגילים". למשל {% equation %}\sqrt{2}{% endequation %}. אנחנו יודעים שלמשוואה {% equation %}x^{2}-2=0{% endequation %} יש שני פתרונות: {% equation %}\sqrt{2}{% endequation %} ו-{% equation %}-\sqrt{2}{% endequation %}, כשהקונבנציה היא ש-{% equation %}\sqrt{2}{% endequation %} הוא הפתרון "החיובי". זה על פניו לא לגמרי מסתדר עם מה שאמרתי לפני רגע על כך שאפשר לסמן כל אחד מהשורשים בתור {% equation %}\sqrt{2}{% endequation %}, אבל זה בגלל שההקשר שבו אנחנו מדברים על {% equation %}\sqrt{2}{% endequation %} בדרך כלל הוא יותר <strong>ספציפי</strong>: זה ההקשר של {% equation %}\mathbb{R}{% endequation %}, שהוא <strong>שדה סדור</strong>. אפשר להשוות דברים ל-0 ולומר אם הם גדולים או קטנים יותר. בהקשר הכללי יותר של שדות זה לא קיים, ואם תחשבו על זה רגע - גם ההגדרה של "חיובי" ו"שלילי" היא מלכתחילה שרירותית. למה "שלילי" הוא מה שנמצא משמאל לציר {% equation %}y{% endequation %} ולא מה שמימין?

הדוגמא הבאה שקל לנו יחסית להבין היא של המשוואה {% equation %}x^{4}=16{% endequation %}. למשוואה הזו יש את הפתרון המתבקש {% equation %}x=2{% endequation %} וגם את {% equation %}x=-2{% endequation %}, אבל כדי לראות את כל הפתרונות צריך לערב גם מרוכבים, ומקבלים את הפתרונות {% equation %}\pm2i{% endequation %}. כלומר, כל פתרון מתקבל מלקיחת אחד מהפתרונות וכפל באברי הקבוצה {% equation %}\left\{ 1,-1,i,-i\right\} {% endequation %} של שורשי היחידה מסדר 4. הדוגמא הזו מעניינת, כי {% equation %}\mathbb{Q}{% endequation %} מכיל חלק מהפתרונות אבל לא את כולם; כדי שנקבל את כל הפתרונות, אנחנו חייבים להוסיף ל-{% equation %}\mathbb{Q}{% endequation %} גם את {% equation %}i{% endequation %}. הייתה לנו סיטואציה דומה בפוסט קודם, עם הפולינום {% equation %}x^{3}-2{% endequation %}; שם השורשים שלו הם {% equation %}\sqrt[3]{2}{% endequation %} ו-{% equation %}\omega_{3}\sqrt[3]{2}{% endequation %} ו-{% equation %}\omega_{3}^{2}\sqrt[3]{2}{% endequation %}. במקרה הזה, {% equation %}\mathbb{Q}\left(\sqrt[3]{2}\right){% endequation %} הוא לא שדה הפיצול של הפולינום, אלא רק {% equation %}\mathbb{Q}\left(\omega_{3},\sqrt[3]{2}\right){% endequation %}. זה מבהיר לנו שאם באופן כללי אנחנו רוצים ש-{% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} תהיה הרחבת גלואה, אז צריך ש-{% equation %}F{% endequation %} <strong>כבר יכיל מראש</strong> את שורשי היחידה מסדר {% equation %}n{% endequation %}. לנו זה לא יפריע בכל מקרה, כי אם {% equation %}F{% endequation %} <strong>לא</strong> מכיל אותן, אפשר לבנות שרשרת של הרחבות: {% equation %}F\subseteq F\left(\omega_{n}\right)\subseteq F\left(\omega_{n}\right)\left(\sqrt[n]{a}\right){% endequation %}. בשרשרת הזו כל איבר התקבל מקודמו על ידי הוספת שורש {% equation %}n{% endequation %}-י של פולינום, ולכן היא עדיין מהווה חלק לגיטימי משרשרת שמראה שהרחבה כלשהי היא רדיקלית. בנוסף לכך, {% equation %}F\left(\omega_{n}\right)/F{% endequation %} היא הרחבת גלואה (<strong>הרחבה ציקלוטומית</strong>) ועכשיו גם {% equation %}F\left(\omega_{n}\right)\left(\sqrt[n]{a}\right)/F\left(\omega_{n}\right){% endequation %} תהיה הרחבת גלואה.

יפה, אז מעכשיו {% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} היא הרחבת גלואה של {% equation %}F{% endequation %}, אבל מה חבורת הגלואה שלה יכולה להיות? אם {% equation %}\sigma{% endequation %} הוא אוטומורפיזם של {% equation %}E{% endequation %} שמשמר את {% equation %}F{% endequation %} אז בפרט הוא משמר את שורשי היחידה. לכן {% equation %}\sigma\left(\omega_{n}^{k}\sqrt[n]{a}\right)=\omega_{n}^{k}\sigma\left(\sqrt[n]{a}\right){% endequation %}, מה שאומר שהערך של {% equation %}\sigma{% endequation %} על <strong>כל</strong> שורש של {% equation %}x^{n}-1{% endequation %} נקבע באופן יחיד על ידי הפעולה שלו על {% equation %}\sqrt[n]{a}{% endequation %}. האם זה אומר שיש {% equation %}n{% endequation %} אוטומורפיזמים, אחד שמעביר את {% equation %}\sqrt[n]{a}{% endequation %} לכל אחד מ-{% equation %}n{% endequation %} השורשים האפשריים של {% equation %}x^{n}-a{% endequation %}? ובכן, לא בהכרח. בואו נסתכל למשל על השדה {% equation %}\mathbb{Q}\left(i\right){% endequation %} - כלומר, אחרי שהוספתי לרציונליים את שורשי היחידה מסדר 4. בשדה הזה ניקח את {% equation %}a=4{% endequation %} ונבנה את ההרחבה {% equation %}\mathbb{Q}\left(i,\sqrt[4]{4}\right)/\mathbb{Q}\left(i\right){% endequation %}. כלומר, הוספנו שורש של הפולינום {% equation %}x^{4}-4{% endequation %}. עכשיו, מכיוון ש-{% equation %}4=2^{2}{% endequation %}, הרי ש-{% equation %}\sqrt[4]{4}=\sqrt{2}{% endequation %}, ולכן אנחנו מקבלים את ההרחבה {% equation %}\mathbb{Q}\left(i,\sqrt{2}\right)/\mathbb{Q}\left(i\right){% endequation %} שהיא במובהק ממימד 2 כי הפולינום המינימלי של {% equation %}\sqrt{2}{% endequation %} מעל {% equation %}\mathbb{Q}{% endequation %} הוא ממעלה 2. כלומר, יש רק שני אוטומורפיזמים. מה השתבש?

ובכן, אם נפרק את {% equation %}x^{4}-4{% endequation %} לגורמים נקבל את הפולינום {% equation %}\left(x-\sqrt{2}\right)\left(x+\sqrt{2}\right)\left(x-i\sqrt{2}\right)\left(x+i\sqrt{2}\right){% endequation %}. בינתיים הכל מתקדם לפי התוכנית - השורשים של הפולינום הם אכן שורש אחד קונקרטי ({% equation %}\sqrt{2}{% endequation %} למשל) כפול שורשי היחידה מסדר 4. רק מה, אם נכפול את זוג הגורמים הראשון והשני, ואת זוג הגורמים השלישי והרביעי, נקבל את הדבר הבא:

{% equation %}\left(x^{2}-2\right)\left(x^{2}+2\right){% endequation %}

זו מכפלה של שני פולינומים ששניהם <strong>כבר שייכים</strong> ל-{% equation %}\mathbb{Q}\left(i\right){% endequation %}. כלומר, {% equation %}x^{4}-4{% endequation %} הוא <strong>פריק</strong> מעל {% equation %}\mathbb{Q}\left(i\right){% endequation %}, למרות שאין לו אף שורש בשדה הזה. תורת גלואה אומרת לנו שכל אוטומורפיזם של השדה מבצע פרמוטציה בין השורשים <strong>של כל גורם אי פריק</strong> של הפולינום; אי אפשר שהוא "יקפיץ" שורש מגורם אי פריק אחד לגורם אי פריק אחר.

והנה הסבר מפורש: נניח ש-{% equation %}\sigma{% endequation %} אוטומורפיזם של {% equation %}\mathbb{Q}\left(i,\sqrt{2}\right){% endequation %} שמשמר את {% equation %}\mathbb{Q}\left(i\right){% endequation %}. נניח לרגע בשלילה ש-{% equation %}\sigma\left(\sqrt{2}\right)=i\sqrt{2}{% endequation %}, אז אם נעלה את שני האגפים בריבוע, נקבל ש-

{% equation %}2=\sigma\left(2\right)=\sigma\left(\sqrt{2}\right)^{2}=\left(i\sqrt{2}\right)^{2}=-2{% endequation %}

וזו סתירה מפורשת שנובעת מכך שכבר הריבוע של ה"יוצר" {% equation %}\sqrt{2}{% endequation %} שלנו שייך לשדה הבסיס ש-{% equation %}\sigma{% endequation %} מחוייבת לשמר.

אז {% equation %}\sigma{% endequation %} לא בהכרח מסוגלת להעביר את {% equation %}\sqrt[n]{a}{% endequation %} <strong>לכל</strong> שורש אחר של {% equation %}x^{n}-a{% endequation %}, אבל כשהיא כן מעבירה את {% equation %}\sqrt[n]{a}{% endequation %} למשהו, זה יהיה לאיבר מהצורה {% equation %}\omega_{n}^{k}\sqrt[n]{a}{% endequation %}. אם {% equation %}\sigma\left(\sqrt[n]{a}\right)=\omega_{n}^{k}\sqrt[n]{a}{% endequation %} אפשר לסמן את {% equation %}\sigma{% endequation %} בתור {% equation %}\sigma_{k}{% endequation %}. קל לראות ש-{% equation %}\sigma_{k}\sigma_{t}=\sigma_{k+t}{% endequation %} כשהחיבור מתבצע מודולו {% equation %}n{% endequation %}, ולכן יש לנו איזומורפיזם בין {% equation %}\text{Gal}\left(F\left(\sqrt[n]{a}\right)/F\right){% endequation %} ובין <strong>תת-חבורה </strong>של {% equation %}\mathbb{Z}_{n}{% endequation %}. תת-חבורה של חבורה ציקלית היא בעצמה ציקלית, מה שמסיים את הכיוון הזה של ההוכחה: הראינו שחבורת גלואה של כל הרחבה רדיקלית היא חבורה ציקלית, בתנאי שהשדה שאותו מרחיבים כבר מכיל את שורשי היחידה הרלוונטיים.
<h2>תגידו יפה שלום לרזולבנטה של לגראנז'</h2>
לפני גלואה וגם לפני אבל ורופיני, לגראנז' כבר התעסק עם התעלומה של פתרון משווואות פולינומיות. לומר מה בדיוק עשה - זה עניין לפוסט נפרד שיעסוק בהיסטוריה של הנושא, אבל אפשר לומר שבזכות לגראנז' היה לבאים אחריו קרש קפיצה אל התגליות היפות שלהם. <strong>משפט לגראנז'</strong> בתורת החבורות נולד מתוך העבודה הזו של לגראנז', וכך גם המושג שאני רוצה לתאר עכשיו - <strong>הרזולבנטה</strong>. שוב, לא אכנס כרגע לשאלה מה בדיוק לגראנז' ניסה להשיג באמצעותה, אלא את מה שהיא הולכת לתת לנו עכשיו - היא תוכיח לנו שאם {% equation %}E/F{% endequation %} היא הרחבת גלואה עם חבורת גלואה {% equation %}\mathbb{Z}_{n}{% endequation %} ו-{% equation %}F{% endequation %} מכיל את שורשי היחידה מסדר {% equation %}n{% endequation %}, והמציין שלו לא מחלק את {% equation %}n{% endequation %} - אז במקרה זה, {% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} עבור {% equation %}a\in F{% endequation %} כלשהו. כלומר, "כל הרחבה ציקלית היא רדיקלית", כאשר "הרחבה ציקלית" זו הרחבה עם חבורת גלואה ציקלית, ואני מטאטא מתחת לשטיח את הפרטים הטכניים של שורשי היחידה והמציין.

אני בעצמי כבר לא זוכר את זה, אבל הזכרתי מתישהו בחטף את המושג של <strong>עקבה</strong> בתורת גלואה - העקבה (Trace) של איבר {% equation %}a\in E{% endequation %} בהרחבת גלואה {% equation %}E/F{% endequation %} הוא הסכום {% equation %}\sum_{\sigma\in\text{Gal}\left(E/F\right)}\sigma\left(a\right){% endequation %}, והפואנטה איתו היא שהוא שייך ל-{% equation %}F{% endequation %}; קל לראות את זה אם מפעילים איבר כללי של חבורת הגלואה של {% equation %}E/F{% endequation %} על הסכום הזה; בזכות התכונות של חבורה, נקבל בדיוק את אותו הסכום שוב, ולכן העקבה שייכת לשדה השבת של חבורת הגלואה של {% equation %}E/F{% endequation %}, שהיא {% equation %}F{% endequation %}.

הרזולבנטה של לגרנאז' מזכירה מאוד את זה, פרט לכך שאנחנו מכניסים לתוך הסכום הזה גם חזקות של שורש יחידה. מכיוון שבמקרה שלנו, {% equation %}\text{Gal}\left(E/F\right){% endequation %} היא ציקלית, אפשר לקחת לה יוצר {% equation %}\sigma{% endequation %} ואז אפשר לכתוב את העקבה בתור {% equation %}\sum_{k=0}^{n-1}\sigma^{k}\left(a\right){% endequation %}. הרזולבנטה תהיה כמעט אותו דבר, אבל כשמכניסים לתמונה {% equation %}\omega{% endequation %} שהוא שורש יחידה מסדר {% equation %}n{% endequation %}:

{% equation %}\left(a,\omega\right)\triangleq\sum_{k=0}^{n-1}\omega^{k}\sigma^{k}\left(a\right)=a+\omega\sigma\left(a\right)+\dots+\omega^{n-1}\sigma^{n-1}\left(a\right){% endequation %}

אם תרצו, אפשר לחשוב על זה כאילו העובדה ש-{% equation %}\text{Gal}\left(E/F\right){% endequation %} היא ציקלית מאפשרת לנו "לתאם" בין החזקות של {% equation %}\omega{% endequation %} ובין האוטומורפיזם שמופעל על {% equation %}a{% endequation %} בכל אחד מהאיברים בסכום.

הרזולבנטה, אם כן, היא איבר ב-{% equation %}E{% endequation %} שמחושב מתוך {% equation %}a,\omega{% endequation %} איכשהו. מה שהולך לעניין אותנו הוא מה קורה לאיבר הזה כשמפעילים עליו את {% equation %}\sigma{% endequation %}, היוצר של חבורת הגלואה של {% equation %}E/F{% endequation %}. מה שיקרה הוא שהסכום שמגדיר את הרזולבנטה "יזוז צעד אחד הצידה":

{% equation %}\sigma\left(\left(a,\omega\right)\right)=\sigma\left(\sum_{k=0}^{n-1}\omega^{k}\sigma^{k}\left(a\right)\right)={% endequation %}

{% equation %}=\sum_{k=0}^{n-1}\omega^{k}\sigma^{k+1}\left(a\right)=\omega^{-1}\sum_{k=0}^{n-1}\omega^{k+1}\sigma^{k+1}\left(a\right){% endequation %}

וכעת מגיע הפאנץ': הציקליות ה"משותפת" הן של {% equation %}\sigma{% endequation %} והן של {% equation %}\omega{% endequation %}, שנובעת מכך ש-{% equation %}\sigma^{n}=\text{id}{% endequation %} ו-{% equation %}\omega^{n}=1{% endequation %}; היא מביאה לכך ש-{% equation %}\omega^{n}\sigma^{n}\left(a\right)=\omega^{0}\sigma^{0}\left(a\right){% endequation %}, ולכן

{% equation %}\omega^{-1}\sum_{k=0}^{n-1}\omega^{k+1}\sigma^{k+1}\left(a\right)=\omega^{-1}\sum_{k=1}^{n}\omega^{k}\sigma^{k}\left(a\right)={% endequation %}

{% equation %}=\omega^{-1}\sum_{k=0}^{n-1}\omega^{k}\sigma^{k}\left(a\right)=\omega^{-1}\left(a,\omega\right){% endequation %}

כלומר, להפעיל את {% equation %}\sigma{% endequation %} על הרזולבנטה זה כמו לכפול אותה ב-{% equation %}\omega^{-1}{% endequation %}. כעת, בואו נסתכל על האיבר {% equation %}\left(a,\omega\right)^{n}{% endequation %}. האיבר הזה הוא הרזולבנטה (הרזולבנטה היא איבר ב-{% equation %}E{% endequation %}) כשמעלים אותה בחזקת {% equation %}n{% endequation %}. מה קורה כשמפעילים את {% equation %}\sigma{% endequation %} על האיבר הזה? ובכן, מקבלים:

{% equation %}\sigma\left(\left(a,\omega\right)^{n}\right)=\left(\sigma\left(a,\omega\right)\right)^{n}=\left(\omega^{-1}\left(a,\omega\right)\right)^{n}={% endequation %}

{% equation %}\left(\omega^{n}\right)^{-1}\left(a,\omega\right)=\left(a,\omega\right){% endequation %}

במילים אחרות, {% equation %}\left(a,\omega\right)^{n}{% endequation %} מקובע על ידי {% equation %}\sigma{% endequation %}, ומכיוון ש-{% equation %}\sigma{% endequation %} יוצרת את כל {% equation %}\text{Gal}\left(E/F\right){% endequation %} אז {% equation %}\left(a,\omega\right)^{n}{% endequation %} שייך לשדה השבת של {% equation %}\text{Gal}\left(E/F\right){% endequation %} ומכיוון שזו הרחבת גלואה אז שדה השבת הזה הוא <strong>בדיוק</strong> {% equation %}F{% endequation %}. קיבלנו ש-{% equation %}\left(a,\omega\right)^{n}\in F{% endequation %}, בדיוק כמו שקורה עם העקבה. עכשיו, מה יש לנו? איבר שהחזקה ה-{% equation %}n{% endequation %}-ית שלו שייכת ל-{% equation %}F{% endequation %}, והוא עצמו שייך ל-{% equation %}E{% endequation %}? זה נותן תחושה ש-{% equation %}\left(a,\omega\right)^{n}{% endequation %} הוא מועמד טוב להיות האיבר שהוספת שורש {% equation %}n{% endequation %}-י שלו יוצרת את כל {% equation %}E{% endequation %} - איבר שאם אוכיח שקיים, הוכחתי ש-{% equation %}E/F{% endequation %} היא הרחבה רדיקלית פרימיטיבית. העניין הוא שאני צריך כאן יותר מאשר תחושה, כי זה פשוט לא יעבוד בהכרח בלי הנחות נוספות. המזל שלי הוא שההגדרה של הרזולבנטה השאירה לי מרחב תמרון בבחירה של ה-{% equation %}a\in E{% endequation %} שיוצר אותה.

בואו נשכח לרגע מרזולבנטה ונשאל שאלה כללית יותר בתורת גלואה: תהא {% equation %}E/F{% endequation %} הרחבת גלואה ויהא {% equation %}a\in E{% endequation %}. מה ישכנע אותנו ש-{% equation %}E=F\left(a\right){% endequation %}? ובכן, הנה דבר אחד שיעבוד: נניח שלכל {% equation %}\sigma\in\text{Gal}\left(E/F\right){% endequation %} כך ש-{% equation %}\sigma\ne\text{id}{% endequation %} מתקיים {% equation %}\sigma\left(a\right)\ne a{% endequation %}, כלומר {% equation %}a{% endequation %} לא מקובע על ידי אף איבר לא טריוויאלי בחבורת הגלואה של {% equation %}E/F{% endequation %}. אני טוען שזה מספיק כדי להוכיח ש-{% equation %}E=F\left(a\right){% endequation %}. למה? ובכן, {% equation %}F\left(a\right)\subseteq E{% endequation %} תמיד, אבל על פי המשפט היסודי של תורת גלואה, {% equation %}\text{Gal}\left(E/F\left(a\right)\right){% endequation %} היא תת-חבורה של {% equation %}\text{Gal}\left(E/F\right){% endequation %}. כל איבר של {% equation %}\text{Gal}\left(E/F\left(a\right)\right){% endequation %} מקבע את כל השדה {% equation %}F\left(a\right){% endequation %} ובפרט מקבע את {% equation %}a{% endequation %}, וכבר אמרנו שהאיבר היחיד שעושה זאת הוא {% equation %}\text{id}{% endequation %}. המסקנה היא ש-{% equation %}\text{Gal}\left(E/F\left(a\right)\right){% endequation %} היא החבורה הטריוויאלית מסדר 1, ולכן {% equation %}\left[E:F\left(a\right)\right]=1{% endequation %}, כלומר {% equation %}E=F\left(a\right){% endequation %}.

חזרה לרזולבנטה - מה שאני צריך לעשות הוא למצוא איברים {% equation %}a,\omega{% endequation %} כך שהרזולבנטה {% equation %}\left(a,\omega\right){% endequation %} תקיים ש-{% equation %}\sigma^{k}\left(\left(a,\omega\right)\right)\ne\left(a,\omega\right){% endequation %} לכל {% equation %}1\le k\le n-1{% endequation %}. זה יוכיח ש-{% equation %}E=F\left(\left(a,\omega\right)\right){% endequation %}, ובמקרה שלנו, אם אגדיר {% equation %}b=\left(a,\omega\right)^{n}{% endequation %} אז {% equation %}b\in F{% endequation %} ואני אקבל ש-{% equation %}E=F\left(\sqrt[n]{b}\right){% endequation %}. מה שיסיים את ההוכחה.

על פניו לא מצפה לנו בעיה מהותית: ראינו כבר ש-{% equation %}\sigma^{k}\left(\left(a,\omega\right)\right)=\omega^{-k}\left(a,\omega\right){% endequation %}, כך שכל מה שעלינו לעשות הוא לבחור את {% equation %}a,\omega{% endequation %} כדי למנוע את האפשרות שיקרה משהו כזה, עבור {% equation %}0\le k&lt;t\le n-1{% endequation %}:

{% equation %}\omega^{-k}\left(a,\omega\right)=\omega^{-t}\left(a,\omega\right){% endequation %}

יש שתי אפשרויות שעלולות לגרום לזה לקרות:
<ul>
 	<li>{% equation %}\omega{% endequation %} אינו שורש יחידה <strong>פרימיטיבי</strong> מסדר {% equation %}n{% endequation %}, כלומר לא כל החזקות {% equation %}\omega^{0},\omega^{1},\omega^{2},\dots,\omega^{n-1}{% endequation %} שונות זו מזו. אין כאן בעיה כי <strong>אני בוחר</strong> איזה {% equation %}\omega{% endequation %} לקחת; אני כן אקח שורש יחידה פרימיטיבי.</li>
 	<li>{% equation %}\left(a,\omega\right)=0{% endequation %}. בואו נדבר על זה.</li>
</ul>
האפשרות שיתקיים {% equation %}\left(a,\omega\right)=0{% endequation %} אינה מופרכת כלל. זה בהחלט קורה, למשל, אם {% equation %}a=1{% endequation %} ואז {% equation %}\left(a,\omega\right)=1+\omega+\dots+\omega^{n-1}=\frac{\omega^{n}-1}{\omega-1}=\frac{1-1}{\omega-1}=0{% endequation %}. למעשה, אני הולך לגייס טיעון כבד משקל כדי לומר שקיים {% equation %}a{% endequation %} עבורו זה <strong>לא</strong> קורה. אם נחשוב על זה לרגע, רזולבנטה היא <strong>צירוף לינארי</strong> של הפעלות של אברי גלואה על {% equation %}a{% endequation %}, כשהמקדמים של הצירוף הלינארי הזה הם החזקות של {% equation %}\omega{% endequation %}. אז בואו נשכח לרגע מ-{% equation %}a{% endequation %} ונסתכל על צירוף לינארי של אוטומורפיזמים:

{% equation %}\sigma^{0}+\omega\sigma+\omega^{2}\sigma^{2}+\dots+\omega^{n-1}\sigma^{n-1}{% endequation %}

העניין הוא <a href="https://gadial.net/2018/05/07/fields_and_groups_collide/">שהוכחתי פה בעבר</a> שאוטומורפיזמים של שדה הם בלתי תלויים לינארית (אפילו לא צריך הרחבת גלואה לשם כך). זה אומר ש-{% equation %}\sigma^{0}+\omega\sigma+\omega^{2}\sigma^{2}+\dots+\omega^{n-1}\sigma^{n-1}\ne0{% endequation %}, כלומר קיים קלט לפונקציה-שהיא-סכום באגף שמאל שלא מאפס אותו. לקלט הזה אקרא {% equation %}a{% endequation %}, ואחרי שאני מציב אותו בסכום אני מקבל בדיוק את {% equation %}\left(a,\omega\right){% endequation %}. זה מסיים את ההוכחה: {% equation %}\left(a,\omega\right){% endequation %} הוא האיבר שיוצר את {% equation %}E/F{% endequation %}.

האם זה מסיים את המשפט של גלואה? הו, אפילו לא קרוב.
<h2>הוכחת המשפט של גלואה</h2>
בואו נזכיר מה <strong>כבר</strong> הוכחנו, ומה אנחנו <strong>רוצים</strong> להוכיח. מה ש<strong>כבר</strong> הוכחנו הוא שאם {% equation %}F{% endequation %} הוא שדה ממציין 0 (אפשר גם מציינים אחרים מסויימים אבל נעזוב את זה) שכולל את כל שורשי היחידה מסדר {% equation %}n{% endequation %}, אז:
<ul>
 	<li>אם {% equation %}E/F{% endequation %} הרחבת גלואה עם חבורת גלואה {% equation %}\mathbb{Z}_{n}{% endequation %} אז {% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} עבור {% equation %}a\in F{% endequation %}.</li>
 	<li>אם {% equation %}E=F\left(\sqrt[n]{a}\right){% endequation %} עבור {% equation %}a\in F{% endequation %} אז {% equation %}E/F{% endequation %} הרחבת גלואה עם חבורת גלואה {% equation %}\mathbb{Z}_{d}{% endequation %} כך ש-{% equation %}d|n{% endequation %}.</li>
</ul>
מה שאנחנו <strong>רוצים</strong> להוכיח הוא משפט שנוגע לפולינומים:
<ul>
 	<li>{% equation %}p\left(x\right){% endequation %} פתיר על ידי רדיקלים אם ורק אם חבורת הגלואה שלו פתירה.</li>
</ul>
נטפל בכל כיוון בנפרד. <strong>לאט מאוד ובזהירות מאוד</strong>.

ובכן, ראשית נניח ש-{% equation %}p\left(x\right){% endequation %} פתיר על ידי רדיקלים. זה אומר שלכל {% equation %}a{% endequation %} בשדה הפיצול של {% equation %}p{% endequation %} שמקיים {% equation %}p\left(a\right)=0{% endequation %}, מתקיים ש-{% equation %}a\in E{% endequation %} כך ש-{% equation %}E/F{% endequation %} הרחבה רדיקלית. בשלב הראשון, נרצה להראות למה אפשר להניח ש-{% equation %}E/F{% endequation %} גלואה עם חבורת גלואה פתירה. השלב הראשון הזה יהיה קשה למדי מבחינה טכנית, אז בואו לא נתייאש.

העובדה ש-{% equation %}E/F{% endequation %} היא הרחבה רדיקלית אומרת לנו בדיוק את הדבר הבא: קיימת סדרת תת-שדות, {% equation %}F=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=E{% endequation %}, כך ש-{% equation %}E_{i+1}=E_{i}\left(\sqrt[k_{i}]{a_{i}}\right){% endequation %} עבור {% equation %}a_{i}\in E_{i}{% endequation %}. מה שאנחנו <strong>לא</strong> יודעים כרגע:
<ul>
 	<li>לא יודעים ש-{% equation %}E/F{% endequation %} היא גלואה בכלל.</li>
 	<li>לא יודעים שב-{% equation %}E_{i}{% endequation %} יש שורשי יחידה.</li>
 	<li>לא יודעים ש-{% equation %}E_{i+1}/E_{i}{% endequation %} היא הרחבה עם חבורת גלואה ציקלית.</li>
</ul>
אנחנו לא יודעים את כל אלו כי הם לא בהכרח נכונים בכלל; אנחנו נרצה לקחת את סדרת ההרחבות הקיימת ולבנות מתוכה סדרה חדשה, טובה יותר, שכן תקיים את כל אלו. ראשית, ניקח <strong>סגור גלואה</strong> {% equation %}K/E{% endequation %}, כלומר את ההרחבה הקטנה ביותר של {% equation %}E{% endequation %} שהיא גלואה מעל {% equation %}F{% endequation %}. עכשיו, אני ארצה להראות שגם {% equation %}K/F{% endequation %} היא הרחבה רדיקלית. לצורך כך תהא {% equation %}G=\text{Gal}\left(K/F\right){% endequation %} ויהא {% equation %}\sigma\in G{% endequation %} ונסתכל על סדרת ההרחבות שמתקבלת מ-{% equation %}E/F{% endequation %} כש"מזיזים את הכל" בעזרת {% equation %}\sigma{% endequation %}: סדרת ההרחבות

{% equation %}F=\sigma\left(E_{0}\right)\subseteq\sigma\left(E_{1}\right)\subseteq\dots\subseteq\sigma\left(E_{n}\right)=\sigma\left(E\right){% endequation %}

אם {% equation %}E_{i+1}=E_{i}\left(\sqrt[k_{i}]{a_{i}}\right){% endequation %} אז {% equation %}\sigma\left(E_{i+1}\right)=\sigma\left(E_{i}\right)\left(\sigma\left(\sqrt[k_{i}]{a_{i}}\right)\right){% endequation %} ולכן גם הסדרה החדשה היא סדרת הרחבות רדיקליות פרימיטיביות ולכן {% equation %}\sigma\left(E\right)/F{% endequation %} הוא אכן הרחבה רדיקלית. איך זה עזר לנו? כי עכשיו אפשר לקחת את <strong>הקומפוזיטום</strong> של כל השדות {% equation %}\sigma\left(E\right){% endequation %} כך ש-{% equation %}\sigma\in G{% endequation %}; הקומפוזיטום הזה הוא השדה הקטן ביותר שמכיל את כל ה-{% equation %}\sigma\left(E\right){% endequation %} הללו. מכיוון ש-{% equation %}K{% endequation %} הוא השדה שמעליו מוגדרים כל האוטומורפיזמים {% equation %}\sigma{% endequation %} הללו, הרי ש-{% equation %}K{% endequation %} מכיל את כל ה-{% equation %}\sigma\left(E\right){% endequation %} הללו ולכן {% equation %}K{% endequation %} מכיל את הקומפוזיטום. מצד שני, כל ה-{% equation %}\sigma{% endequation %}-ות הללו הן אוטומורפיזמים של הקומפוזיטום (זה, כמובן, תרגיל לא טריוויאלי בפני עצמו) כך שגודל חבורת האוטומורפיזמים של הקומפוזיטום שמשמרים את {% equation %}F{% endequation %} הוא <strong>לפחות</strong> המימד שלו מכל {% equation %}F{% endequation %} - זה גורר שהוא חייב להיות שווה ל-{% equation %}K{% endequation %} עצמו.

זה עדיין לא מסיים את השלב הזה, כי אני רוצה לומר ש-{% equation %}K{% endequation %} הוא הרחבה רדיקלית, וכרגע ראיתי רק שהוא קומפוזיטום של הרחבות רדיקליות. מכיוון שלקחתי קומפוזיטום של מספר סופי של הרחבות, מספיק להסביר למה עובד עבור שתיים ומכאן להמשיך באינדוקציה. ובכן, בואו ניקח שתי הרחבות רדיקליות של שדה {% equation %}F{% endequation %}:

{% equation %}F=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=E{% endequation %}

{% equation %}F=K_{0}\subseteq K_{1}\subseteq K_{2}\subseteq\dots\subseteq K_{m}=K{% endequation %}

אני רוצה להראות ש-{% equation %}EK/F{% endequation %} רדיקלית. ראשית, שימו לב לכך שאם אני מצרף את {% equation %}K_{1}{% endequation %} לכל השדות בהרחבה הראשונה, עדיין קיבלתי הרחבה רדיקלית:

{% equation %}F\subseteq E_{0}K_{1}\subseteq E_{1}K_{1}\subseteq E_{2}K_{1}\subseteq\dots\subseteq E_{n}K_{1}=EK_{1}{% endequation %}

זה עובד מהסיבה הבאה: {% equation %}E_{0}K_{1}/F{% endequation %} זו פשוט ההרחבה {% equation %}K_{1}/F{% endequation %} (הרי {% equation %}E_{0}=F\subseteq K_{1}{% endequation %}) שאנחנו יודעים שהיא רדיקלית פרימיטיבית. כעת, {% equation %}E_{i+1}K_{1}/E_{i}K_{1}{% endequation %} היא רדיקלית פרימיטיבית מאותה הסיבה ש-{% equation %}E_{i+1}/E_{i}{% endequation %} היא כזו: {% equation %}E_{i+1}K_{1}=E_{i}K_{1}\left(\sqrt[k_{i}]{a_{i}}\right){% endequation %}. כך זה ימשיך לעבוד לכל אורך סדרת השדות, ונקבל ש-{% equation %}EK_{1}/F{% endequation %} היא רדיקלית. ואז נעשה את זה שוב, ונקבל ש-{% equation %}EK_{1}K_{2}=EK_{2}{% endequation %} רדיקלית, וכן הלאה עד ל-{% equation %}EK/F{% endequation %}. זה מסיים, בנפנוף ידיים, את הטענה הבאה:
<ul>
 	<li>אם {% equation %}E/F{% endequation %} הרחבה רדיקלית ניתן להניח שהיא גלואה.</li>
</ul>
עכשיו צריך לדבר על שורשי יחידה. כמקודם, מה שיש לנו כרגע הוא סדרה של הרחבות:

{% equation %}F=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=E{% endequation %}

כל הרחבה מתקבלת מקודמתה על ידי הוספת שורש: {% equation %}E_{i+1}=E_{i}\left(\sqrt[k_{i}]{a_{i}}\right){% endequation %}. מי שחשוב לי פה הוא ה-{% equation %}k_{i}{% endequation %} - הסדר של השורש שהוספנו. כדי שהכל יתנהג נחמד בהמשך, אני אצטרך ש-{% equation %}F{% endequation %} כבר יכיל את שורשי היחידה מסדר {% equation %}k_{i}{% endequation %}. אז אני אוסיף ל-{% equation %}F{% endequation %} את שורשי היחידה מסדר {% equation %}k_{i}{% endequation %} <strong>לכל</strong> {% equation %}k_{i}{% endequation %} בסדרה (למשל, נוסיף את שורשי היחידה מסדר 3, 8 ו-11 אם ההרחבות בוצעו בעזרת {% equation %}\sqrt[3]{a_{1}}{% endequation %} ו-{% equation %}\sqrt[8]{a_{2}}{% endequation %} ו-{% equation %}\sqrt[11]{a_{3}}{% endequation %}). ונקבל שדה חדש {% equation %}F^{\prime}{% endequation %}. ההרחבה {% equation %}F^{\prime}/F{% endequation %} היא כמובן רדיקלית (היא התקבלה משרשרת של הוספת שורשים) ולכן נשאר להראות שההרחבה הבאה רדיקלית:

{% equation %}F^{\prime}=F^{\prime}E_{0}\subseteq F^{\prime}E_{1}\subseteq F^{\prime}E_{2}\subseteq\dots\subseteq F^{\prime}E_{n}=F^{\prime}E{% endequation %}

הרדיקליות של ההרחבה נובעת מאותם טיעונים כמו קודם. מה שצריך להיזהר הוא שלא נאבד את זה שההרחבה היא <strong>גלואה</strong>; זה נובע מכך ש-{% equation %}F^{\prime}/F{% endequation %} היא גלואה (כי {% equation %}F^{\prime}{% endequation %} הוא שדה הפיצול של הפולינום ששורשיו הם כל שורשי היחידה הרלוונטיים) ומכך שקומפוזיטום של הרחבות גלואה הוא הרחבת גלואה (את זה הוכחתי <a href="https://gadial.net/2018/06/30/finite_fields_and_primitive_element_theorem/">בפוסט הקודם</a>).

אז סיימנו את הטענה הבאה:
<ul>
 	<li>אם {% equation %}E/F{% endequation %} רדיקלית אז אפשר להניח ש-{% equation %}E/F{% endequation %} גלואה ו-{% equation %}F{% endequation %} כולל את כל שורשי היחידה מהסדר שמתאים להרחבות הרדיקליות הפרימיטיביות ב-{% equation %}E/F{% endequation %}.</li>
</ul>
המסקנה היא שאם {% equation %}F=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=E{% endequation %} היא סדרת ההרחבות הרלוונטית, אז {% equation %}E_{i+1}/E_{i}{% endequation %} היא הרחבה ציקלית.

האם סיימנו? <strong>עדיין לא</strong>. מה שהוכחנו הוא שאם {% equation %}a{% endequation %} הוא שורש <strong>כלשהו</strong> של הפולינום {% equation %}p\left(x\right){% endequation %} אז קיימת לו הרחבה רדיקלית עם התכונות היפות שתיארנו. אבל אנחנו רוצים הרחבה שתעבוד עבור <strong>כל השורשים</strong> של {% equation %}p\left(x\right){% endequation %} בו-זמנית. התעלול הוא שוב ביצוע קומפוזיטום של הרחבות באופן הדרגתי, כפי שתיארתי קודם, וזה באמת מסיים. אני יכול לטעון את הטענה הבאה:
<ul>
 	<li>אם {% equation %}p\left(x\right){% endequation %} פתיר על ידי רדיקלים אז קיימת הרחבת גלואה {% equation %}E/F{% endequation %} שכוללת את כל שורשי {% equation %}p\left(x\right){% endequation %}, וקיימת סדרת תת-שדות {% equation %}F=E_{0}\subseteq E_{1}\subseteq E_{2}\subseteq\dots\subseteq E_{n}=E{% endequation %} כך שההרחבה {% equation %}E_{i+1}/E_{i}{% endequation %} ציקלית לכל {% equation %}0\le i&lt;n{% endequation %}.</li>
</ul>
בואו נסמן {% equation %}G=\text{Gal}\left(E/F\right){% endequation %} ו-{% equation %}G_{i}=\text{Gal}\left(E/E_{i}\right){% endequation %}. כלומר, קיבלנו סדרה של תת-חבורות {% equation %}\left\{ e\right\} =G_{n}\subseteq G_{n-1}\subseteq\dots\subseteq G_{0}=G{% endequation %}.

עכשיו, בואו וניזכר במשפט היסודי של תורת גלואה. המשפט הזה אומר לנו שעבור מגדל ההרחבות הבא:

{% equation %}E_{i}\subseteq E_{i+1}\subseteq E{% endequation %}

מתקיים הקשר הבא בין חבורות הגלואה הרלוונטיות:

{% equation %}\text{Gal}\left(E_{i+1}/E_{i}\right)\cong\text{Gal}\left(E/E_{i}\right)/\text{Gal}\left(E/E_{i+1}\right)=G_{i}/G_{i+1}{% endequation %}

מכיוון שבמקרה שלנו אנחנו יודעים ש-{% equation %}\text{Gal}\left(E_{i+1}/E_{i}\right){% endequation %} היא ציקלית, המסקנה היא ש-{% equation %}G_{i}/G_{i+1}{% endequation %} היא ציקלית. כעת, הנה טענה שאני דוחה לפוסט הבא, כי היא טענה בתורת החבורות נטו:
<ul>
 	<li>אם {% equation %}G{% endequation %} חבורה <strong>סופית</strong> אז {% equation %}G{% endequation %} פתירה אם ורק אם קיימת סדרה של תת-חבורות {% equation %}\left\{ e\right\} =G_{0}\subseteq G_{1}\subseteq G_{2}\subseteq\dots\subseteq G_{n}=G{% endequation %} כך ש-{% equation %}G_{i+1}/G_{i}{% endequation %} ציקלית לכל {% equation %}0\le i&lt;n{% endequation %} (שימו לב שהפכתי פה את האינדקסים).</li>
</ul>
אז נהדר! קיבלנו ש-{% equation %}G{% endequation %} שלנו פתירה! האם סיימנו? ובכן <strong>לא! </strong>

המשפט שאני רוצה להוכיח הוא:
<ul>
 	<li>אם {% equation %}p\left(x\right){% endequation %} פתיר על ידי רדיקלים אז חבורת הגלואה של {% equation %}p\left(x\right){% endequation %} פתירה.</li>
</ul>
מה שהוכחתי כרגע היה:
<ul>
 	<li>אם {% equation %}p\left(x\right){% endequation %} פתיר על ידי רדיקלים אז שדה הפיצול של {% equation %}p\left(x\right){% endequation %} מוכל בשדה {% equation %}E{% endequation %} כך ש-{% equation %}E/F{% endequation %} הרחבת גלואה עם חבורת גלואה פתירה.</li>
</ul>
אנחנו רוצים להראות שזו חבורת הגלואה <strong>של שדה הפיצול</strong> שפתירה. שדה הפיצול הוא תת-שדה, {% equation %}F\subseteq K\subseteq E{% endequation %}, הוא לא בהכרח שווה ל-{% equation %}E{% endequation %}. בשלב הזה כבר מתחשק לי לבכות, אבל האמת היא שהמצב לא נורא במיוחד. אני יודע בזכות המשפט היסודי שש-{% equation %}\text{Gal}\left(K/F\right)\cong\text{Gal}\left(E/F\right)/\text{Gal}\left(E/K\right){% endequation %}, ואני יודע ש-{% equation %}\text{Gal}\left(E/F\right){% endequation %} היא כן חבורה פתירה. כל מה שנשאר לי לעשות הוא לדחות לפוסט הבא את הוכחת הטענה
<ul>
 	<li>חבורת מנה של חבורה פתירה היא חבורת פתירה.</li>
</ul>
ועכשיו באמת סיימתי! כלומר, סיימתי כיוון <strong>אחד</strong> של ההוכחה. יש גם כיוון שני, קל יותר:
<ul>
 	<li>אם חבורת הגלואה של {% equation %}p\left(x\right){% endequation %} פתירה, אז {% equation %}p\left(x\right){% endequation %} פתיר על ידי רדיקלים.</li>
</ul>
ההוכחה מאוד מזכירה את הכיוון הקודם. נסמן את שדה הפיצול של {% equation %}p\left(x\right){% endequation %} בתור {% equation %}E{% endequation %}, אז ההרחבה {% equation %}E/F{% endequation %} היא בעלת חבורת גלואה פתירה {% equation %}G{% endequation %}. תוך שימוש בטענה שחבורה סופית היא פתירה אם ורק אם קיימת שרשרת חבורות שמקיימת כך וכך, נקבל שיש {% equation %}\left\{ e\right\} =G_{n}\subseteq G_{n-1}\subseteq\dots\subseteq G_{0}=G{% endequation %} כך ש-{% equation %}G_{i}/G_{i+1}{% endequation %} ציקלית. עכשיו נגדיר את {% equation %}E_{i}{% endequation %} להיות שדה השבת ב-{% equation %}E{% endequation %} של {% equation %}G_{i}{% endequation %}, ונקבל סדרה של שדות {% equation %}F=E_{0}\subseteq E_{1}\subseteq\dots\subseteq E_{n}=E{% endequation %} כמקודם. הדבר היחיד שמונע ממני להגדיר שזו שרשרת הרחבות רדיקלית היא העובדה שבשדות הללו לא בהכרח יש את שורשי היחידה המתאימים, אז מה שנעשה הוא לנקוט באותו תעלול כמו קודם - נרחיב את {% equation %}F{% endequation %} על ידי הוספת כל שורשי היחידה הדרושים, ונקבל שדה {% equation %}F\subseteq F^{\prime}{% endequation %}, ושרשרת ההרחבות שלנו תיראה כעת כך:

{% equation %}F\subseteq E_{0}F^{\prime}\subseteq E_{1}F^{\prime}\subseteq\dots\subseteq E_{n}F^{\prime}=EF^{\prime}{% endequation %}

כדי לסיים, צריך להשתכנע שכל ההרחבות הן עדיין הרחבות גלואה, ושחבורת הגלואה של כל זוג הרחבות ביניים היא עדיין ציקלית, ואז נוכל להשתמש במשפט שראינו קודם שמבטיח שכל הרחבה מתקבלת מקודמתה על ידי הוספת שורש.

זה נותן לנו מוטיבציה למשפט בסיסי בתורת גלואה שעד כה לא טרחתי להראות כי לא היה ברור למה הוא מעניין בכלל, והוא הולך כך: אם {% equation %}E/F{% endequation %} היא הרחבת גלואה כלשהי, ו-{% equation %}F^{\prime}/F{% endequation %} היא הרחבה (לאו דווקא גלואה) של שדה הבסיס, אז {% equation %}EF^{\prime}/F^{\prime}{% endequation %} היא הרחבת גלואה, וחבורת גלואה שלה היא {% equation %}\text{Gal}\left(EF^{\prime}/F^{\prime}\right)\cong\text{Gal}\left(E/E\cap F^{\prime}\right){% endequation %}. איך זה מועיל לנו? ובכן, במקרה שלנו זה אומר שיתקיים

{% equation %}\text{Gal}\left(E_{i+1}F^{\prime}/E_{i}F^{\prime}\right)\cong\text{Gal}\left(E_{i+1}/E_{i+1}\cap E_{i}F^{\prime}\right){% endequation %}

(כאן "שדה הבסיס" היה {% equation %}E_{i}{% endequation %} וההרחבה שלו הייתה {% equation %}E_{i}F^{\prime}{% endequation %}; מכיוון ש-{% equation %}E_{i}\subseteq E_{i+1}{% endequation %} אז הקומפוזיטום של {% equation %}E_{i+1}{% endequation %} עם {% equation %}E_{i}F^{\prime}{% endequation %} הוא פשוט {% equation %}E_{i+1}F^{\prime}{% endequation %}).

עכשיו, החבורה {% equation %}\text{Gal}\left(E_{i+1}/E_{i+1}\cap E_{i}F^{\prime}\right){% endequation %} היא חבורת אוטומורפיזמים של {% equation %}E_{i+1}{% endequation %} שמקבעים "קצת יותר מאשר את {% equation %}E_{i}{% endequation %} בלבד", כלומר תת-חבורה של {% equation %}\text{Gal}\left(E_{i+1}/E_{i}\right){% endequation %}. מכיוון שאנחנו כבר יודעים ש-{% equation %}\text{Gal}\left(E_{i+1}/E_{i}\right){% endequation %} ציקלית, זה מוכיח שגם {% equation %}\text{Gal}\left(E_{i+1}F^{\prime}/E_{i}F^{\prime}\right){% endequation %} ציקלית (תת-חבורה של חבורה ציקלית היא ציקלית), מה שמסיים את ההוכחה עד כדי המשפט שטרם הוכחתי על כך ש-{% equation %}\text{Gal}\left(EF^{\prime}/F^{\prime}\right)\cong\text{Gal}\left(E/E\cap F^{\prime}\right){% endequation %}.

אז בואו נוכיח את המשפט הזה ונסיים את הפוסט.

ראשית, להוכיח שאם {% equation %}E/F{% endequation %} גלואה אז גם {% equation %}EF^{\prime}/F^{\prime}{% endequation %} גלואה זה קל. לכאורה העובדה ש-{% equation %}F^{\prime}/F{% endequation %} לא גלואה עלולה להקשות עלינו, אבל לא באמת. העובדה ש-{% equation %}E/F{% endequation %} גלואה אומרת ש-{% equation %}E{% endequation %} הוא שדה פיצול של פולינום {% equation %}p\left(x\right)\in F\left[x\right]{% endequation %}. <strong>אותו פולינום בדיוק</strong> הוא גם איבר של {% equation %}F^{\prime}\left[x\right]{% endequation %} ושדה הפיצול שלו הוא {% equation %}EF^{\prime}{% endequation %} (השדה שמתקבל מלקיחת כל האיברים של {% equation %}F^{\prime}{% endequation %} ובנוסף השורשים של {% equation %}p\left(x\right){% endequation %}). החלק המעניין הוא להבין מהי חבורת הגלואה {% equation %}\text{Gal}\left(EF^{\prime}/F^{\prime}\right){% endequation %}. כל איבר {% equation %}\sigma\in\text{Gal}\left(EF^{\prime}/F^{\prime}\right){% endequation %} הוא אוטומורפיזם של {% equation %}EF^{\prime}{% endequation %}, ואפשר לשאול את עצמנו מה קורה כשהוא מצומצם ל-{% equation %}E{% endequation %}, כלומר מה קורה עם {% equation %}\sigma|_{E}{% endequation %}. הפונקציה הזו היא פונקציה חח"ע מ-{% equation %}E{% endequation %} לתוך {% equation %}EF^{\prime}{% endequation %} - זה מה שנקרא <strong>שיכון</strong>. רק מה, כשהוכחנו את המשפט היסודי של תורת גלואה, ראינו שאם {% equation %}E/F{% endequation %} גלואה, אז כל שיכון מתוך {% equation %}E{% endequation %} שמשמר את {% equation %}F{% endequation %} הוא בהכרח אוטומורפיזם של {% equation %}E{% endequation %} (זה לא היה טריוויאלי לגמרי להוכחה). במקרה שלנו {% equation %}\sigma|_{E}{% endequation %} משמר את {% equation %}F^{\prime}{% endequation %} אז הוא בוודאי משמר גם את {% equation %}F{% endequation %}, ולכן הוא אוטומורפיזם של {% equation %}E{% endequation %}. אם כן, קיבלנו הומומורפיזם של חבורות {% equation %}\varphi:\text{Gal}\left(EF^{\prime}/F^{\prime}\right)\to\text{Gal}\left(E/F\right){% endequation %} שמוגדר על ידי {% equation %}\varphi\left(\sigma\right)=\sigma|_{E}{% endequation %}.

אני רוצה להראות שההתאמה הזו היא חח"ע, אז לשם כך בואו נבין מהו {% equation %}\ker\varphi=\left\{ \sigma\in\text{Gal}\left(EF^{\prime}/F^{\prime}\right)\ |\ \sigma|_{E}=\text{id}\right\} {% endequation %}. אני טוען שהאיבר היחיד ב-{% equation %}\ker\varphi{% endequation %} יכול להיות אוטומורפיזם הזהות על {% equation %}EF^{\prime}{% endequation %}. למה? כי {% equation %}\sigma\in\ker\varphi{% endequation %} אומר ש-{% equation %}\sigma{% endequation %} הוא הזהות הן על השדה {% equation %}E{% endequation %} והן על השדה {% equation %}F^{\prime}{% endequation %} (כי {% equation %}F^{\prime}{% endequation %} הוא שדה הבסיס בהרחבת הגלואה {% equation %}EF^{\prime}/F^{\prime}{% endequation %} שמהחבורה שלה נלקח {% equation %}\sigma{% endequation %}). אם הוא הזהות על שני השדות שמרכיבים את {% equation %}EF^{\prime}{% endequation %} הוא חייב להיות הזהות על כל {% equation %}EF^{\prime}{% endequation %}, אחרת היינו מקבלים ששדה השבת שלו הוא תת-שדה ממש של {% equation %}EF^{\prime}{% endequation %} שמכיל את {% equation %}E,F^{\prime}{% endequation %}, בסתירה למינימליות של {% equation %}EF^{\prime}{% endequation %}. זה מראה לנו ש-{% equation %}\varphi{% endequation %} חח"ע. נשאר רק להשתכנע שהתמונה שלו היא בדיוק {% equation %}\text{Gal}\left(E/E\cap F^{\prime}\right){% endequation %}.

בואו נסמן את התמונה ב-{% equation %}H{% endequation %}. זו חבורה של אוטומורפיזמים של {% equation %}E{% endequation %}, ולכן יש לה שדה שבת, {% equation %}E_{H}{% endequation %}, שאנחנו רוצים להשתכנע שהוא בדיוק {% equation %}E\cap F^{\prime}{% endequation %}. ההכלה {% equation %}E_{H}\supseteq E\cap F^{\prime}{% endequation %} טריוויאלית: אנחנו יודעים שכל איבר של {% equation %}H{% endequation %} הוא צמצום של אוטומורפיזם שהוא הזהות על כל {% equation %}F^{\prime}{% endequation %}; אז גם על האיברים של {% equation %}F^{\prime}{% endequation %} שעדיין בתחום שלו אחרי שהצטמצמנו ל-{% equation %}E{% endequation %} הוא עדיין יהיה הזהות, מה שאומר שהוא בוודאי הזהות על כל {% equation %}E\cap F^{\prime}{% endequation %}. הכיוון השני הוא המעניין יותר.

מכיוון ש-{% equation %}E_{H}\subseteq E{% endequation %} באופן טריוויאלי, רק צריך להשתכנע ש-{% equation %}E_{H}\subseteq F^{\prime}{% endequation %}. כאן מגיע תעלול: נסתכל על הקומפוזיטום {% equation %}E_{H}F^{\prime}{% endequation %}. זה תת-שדה של {% equation %}EF^{\prime}{% endequation %}, ואנחנו יודעים שכל {% equation %}\sigma\in\text{Gal}\left(EF^{\prime}/F^{\prime}\right){% endequation %} משמרת אותו (שוב, כי היא הזהות על {% equation %}E_{H}{% endequation %} ועל {% equation %}F^{\prime}{% endequation %}). כלומר, {% equation %}E_{H}F^{\prime}{% endequation %} משתמר על ידי <strong>כל</strong> חבורת הגלואה {% equation %}\text{Gal}\left(EF^{\prime}/F^{\prime}\right){% endequation %}. אבל כבר ראינו שהרעיון בחבורת גלואה הוא שהשדה שהיא משמרת הוא בדיוק שדה הבסיס של ההרחבה, ולכן {% equation %}E_{H}F^{\prime}=F^{\prime}{% endequation %}. זה יכול לקרות אם ורק אם {% equation %}E_{H}\subseteq F^{\prime}{% endequation %}, מה שמסיים את ההוכחה.
<h2>דברי סיכום והסבר לאן פנינו מועדות</h2>
זהו! הוכחנו את המשפט הכבד ביותר שרציתי להוכיח בתורת גלואה! אבל האם הוכחתי כבר את עניין ה"אין פתרון על ידי רדיקלים למשוואה ממעלה חמישית ומעלה"? לא.

הוכחתי לעת עתה את המשפט "פולינום {% equation %}p\left(x\right){% endequation %} הוא פתיר על ידי רדיקלים אם ורק אם חבורת גלואה שלו פתירה". זה המשפט המרכזי של גלואה והוא יפהפה, אבל כרגע עוד לא יישמתי אותו לשום מקרה מעשי. אני יכול לקחת פולינום ספציפי ממעלה חמישית, לחשב את חבורת הגלואה שלו, להוכיח שהיא לא פתירה ולסיים בזאת; אבל למען האמת, לטפל בפולינום <strong>כללי</strong> ממעלה חמישית ומעלה זה אפילו יותר פשוט, וגם יותר טוב לאינטואיציה (שכרגע אולי עדיין תוהה מה זה בעצם אומר, פולינום כללי). אז זה משהו שאטפל בו בהמשך, אחרי פוסט של תורת החבורות שיסביר לנו אחת ולתמיד את כל מה שאנחנו צריכים לדעת על חבורות פתירות בהקשר הזה. יהיה כיף.
