---
title: "חישוב קוונטי בגישה מתמטית, חלק א'"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
description: 'בואו ניתן עוד סיבוב על חישוב קוונטי, הפעם עם אקסטרה אלגברה לינארית!'
image: "2022/quantum_computer.png"
---


<h2>מבוא</h2>

כבר כתבתי בעבר <a href="https://gadial.net/2014/07/17/quantum_computing_intro/">סדרת פוסטים</a> על חישוב קוונטי, אבל מאז עבר קצת זמן והתחלתי להתעסק באופן אישי בצורה טכנית יותר, וזו הזדמנות טובה לחזור אל הנושא ולהתעמק יותר באספקטים המתמטיים שלו. אני לא אחזור יותר מדי על המוטביציות וההסברים שהיו בסדרת הפוסטים ההיא כי הם בסדר גמור לטעמי, ובפוסטים כאן אני אגש יותר מהר אל התכל'ס. עוד דבר שהכתיב את אופי סדרת הפוסטים ההיא היה דגש על אלגוריתמים קוונטיים - היעד היה להגיע אל האלגוריתם של שור. בסדרה הנוכחית אני כנראה אחזור אליו לביקור, אבל יש הרבה דברים אחרים שאני רוצה להציג.

נתחיל בכל זאת מהסבר כללי מה זה בעצם חישוב קוונטי. בחישוב רגיל (מה שאני אכנה מעכשיו "קלאסי") אבן הבניין הבסיסית שלנו היא משהו שנקרא <strong>ביט</strong>. ביט יכול להיות או 0 או 1, ואנחנו יודעים לעשות מניפולציות על ביטים שנקראות <strong>פעולות לוגיות</strong>, למשל פעולת AND שמקבלת שני ביטים כקלט ומוציאה ביט בודד כפלט, כך שהיא מחזירה 1 רק אם שני הקלטים היו 1 ואחרת היא מחזירה 0. מה שמדהים במדעי המחשב הוא שכל אלגוריתם שרץ בפועל על מחשב ניתן לתרגום אל זה - פעולות לוגיות על מספר קטן של ביטים. זה ממש פשוט. ממש <strong>ממש</strong> פשוט.

חישוב קוונטי שואל את השאלה: אוקיי, האם ייתכן שזה פשוט <strong>מדי</strong>? אולי אפשר לעבור להשתמש באבן בניין בסיסית שתאפשר לנו לעשות קסמים יותר מורכבים? והתשובה היא "כן ולא".

כמובן, חישוב רגיל הוא קצת יותר מסובך מסתם מניפולציות על ביטים. ראשית, כי מעבדים מודרניים יכולים לעשות פעולות מורכבות יחסית שמערבים מספר גדול של ביטים בבת אחת, לרוב תוך שימוש במעגלים מתוחכמים למדי (למשל, פעולת חילוק של מספרים גדולים יחסית). שנית, ורלוונטי יותר לנו, כי בטבע אין ביטים שמתרוצצים אנה ואנה ומחכים שנפעל עליהם. כדי שיהיו לנו ביטים ונבצע עליהם מניפולציות, אנחנו צריכים <strong>לממש</strong> אותם איכשהו. במעבדים מודרניים זה מתבצע באמצעות מניפולציה של חשמל; ביטים ממומשים בעזרת מתח חשמלי, כשהערכים 0 ו-1 מיוצגים על ידי רמות שונות של מתח כזה, ואנחנו משתמשים ברכיבים אלקטרוניים שנקראים טרנזיסטורים כדי לבצע את הפעולות הלוגיות. מה שמעניין פה הוא הרדוקציה הזו של הפיזיקה המורכבת של הטבע, שבעזרת הנדסת חשמל הופכת למשהו מאוד פשוט - 0 ו-1 ופעולות לוגיות, וזהו.

בחישוב קוונטי עדיין מנסים לעשות רדוקציה למורכבות של הטבע אל דבר שהוא יחסית פשוט מבחינה מתמטית. אבל מנסים לשמר קצת יותר מהמורכבות של התופעה שעליה מתבססים - תופעה שבתורת הקוונטים נקראת <strong>סופרפוזיציה</strong> והיא משונה מאוד וממש לא תואמת את החוויה היומיומית שלנו, אבל נוכחנו לדעת שהיא מתארת במדויק את מה שקורה בפיזיקה של סדרי גודל קטנים. השאלה אילו תופעות טבע בדיוק מגוייסות לצורך מימוש של חישוב קוונטי ואיך זה עובד היא מרתקת ואפשר לכתוב פוסטים רבים על שיטות המימוש השונות והמשונות ושלל הבעיות, האתגרים והקירובים שכל שיטה כזו מצריכה, אבל אני במוצהר מתעלם מכל זה ומתחיל מיחידת הבסיסי של חישוב קוונטי: <strong>קיוביט</strong>.

<h2>התיאור המתמטי של קיוביט</h2>

ביט רגיל היה דרך לקחת מערכת פיזיקלית מסובכת ואיכשהו לקבל ממנה מערכת שיש לה רק שני מצבים מובחנים, 0 ו-1. קיוביט הוא דרך לקחת מערכת פיזיקלית מסובכת ואיכשהו לקבל ממנה מערכת שכל המצבים שלה הם <strong>סופרפוזיציה</strong> של שני מצבים מובחנים, שמסמנים {% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %}. מה זו סופרפוזיציה? ובכן, הדרך הטובה ביותר לתאר את זה היא פשוט באמצעות מתמטיקה. ספציפית, אלגברה לינארית (שאני מניח שאתן מכירות).

הסימון {% equation %}\mathbb{C}^{2}{% endequation %} מתאר <strong>מרחב וקטורי</strong> ממימד 2 מעל המרוכבים, שאנחנו מסמנים את מצביו בדרך כלל בתור וקטורי עמודה {% equation %}\left(\begin{array}{c} a\\ b \end{array}\right){% endequation %} כך ש-{% equation %}a,b\in\mathbb{C}{% endequation %}. על המרחב הזה מוגדרת <strong>מכפלה פנימית</strong> סטנדרטית, {% equation %}\left\langle v|u\right\rangle \triangleq\overline{a_{v}}a_{u}+\overline{b_{v}}b_{u}{% endequation %} והמרחב שמתקבל נקרא <strong>מרחב מכפלה פנימית</strong>. רוב מה שאגיד עכשיו נכון למרחבי מכפלה פנימית באופן כללי, אבל כדאי שיהיה לנו בראש את המקרה הקונקרטי של {% equation %}\mathbb{C}^{2}{% endequation %} שממנו מתחילים, ועוד נראה בהמשך איך מתקדמים משם.

עכשיו שווה להציג את שיטת הסימון של איברים שבה ננקוט מכאן והלאה, שנקראת <strong>הסימון של דיראק</strong>. לוקח קצת זמן להתרגל אליה, אבל היא מפשטת מאוד את האינטואיציה כשיש חישובים טכניים ולכן אני בעדה. אינטואיטיבית, אנחנו מסתכלים על הסימון {% equation %}\left\langle v|u\right\rangle {% endequation %} שמתאר מכפלה פנימית של שני איברים, ו"מפרקים" אותו לשניים: {% equation %}\left|u\right\rangle {% endequation %} ו-{% equation %}\left\langle v\right|{% endequation %}. הסימן {% equation %}\left|u\right\rangle {% endequation %} מתאר פשוט וקטור - איבר רגיל של {% equation %}\mathbb{C}^{2}{% endequation %}, בזמן ש-{% equation %}\left\langle v\right|{% endequation %} מתאר את מה שאפשר לקבל מהוקטור {% equation %}\left|v\right\rangle {% endequation %} אם ניקח את מה שנקרא <strong>הצמוד ההרמיטי</strong> שלו - מה שמתקבל משחלוף של הוקטור ואז הצמדה של הכניסות שלו ("שחלוף", transpose באנגלית, נשמע כמו משהו מוכר? אם לא, זו אינדיקציה שאולי כדאי לחזור טיפה על אלגברה לינארית). במילים אחרות, אם {% equation %}\left|v\right\rangle =\left(\begin{array}{c} a\\ b \end{array}\right){% endequation %} אז {% equation %}\left\langle v\right|=\left(\left|v\right\rangle \right)^{*}=\left(\begin{array}{cc} \overline{a} & \overline{b}\end{array}\right){% endequation %}. כעת, אם נזכור כיצד מוגדר כפל של מטריצות, קל לראות ש-{% equation %}\left\langle v\right|\cdot\left|u\right\rangle {% endequation %}, כשכופלים אותם כמו מטריצות (מטריצה {% equation %}1\times2{% endequation %} כפול מטריצה {% equation %}2\times1{% endequation %}) מקבלים בדיוק את המכפלה הפנימית, {% equation %}\left\langle v|u\right\rangle {% endequation %} - הסימון {% equation %}\left\langle v|u\right\rangle {% endequation %} "מסכים" עם הפירוק שלנו {% equation %}\left\langle v\right|\left|u\right\rangle {% endequation %}.

אפשר לחשוב על הסימון הזה גם בצורה יותר מופשטת. מרגע שיש לנו מרחב מכפלה פנימית <strong>כלשהו</strong> {% equation %}V{% endequation %} מעל {% equation %}\mathbb{C}{% endequation %} (או {% equation %}\mathbb{R}{% endequation %}, אבל בהקשר של חישוב קוונטי אנחנו תמיד מעל {% equation %}\mathbb{C}{% endequation %}), אנחנו מסוגלים לחשוב על וקטורים {% equation %}v\in V{% endequation %} כאילו הם מגדירים <strong>פונקציונל לינארי</strong>, כלומר טרנספורמציה לינארית {% equation %}f_{v}:V\to\mathbb{C}{% endequation %}, שמוגדרת על ידי {% equation %}f_{v}\left(u\right)=\left\langle v|u\right\rangle {% endequation %}. אם כן, אפשר לחשוב על {% equation %}\left\langle v\right|{% endequation %} גם בתור פונקציונל לינארי, שהפעולה שלו על {% equation %}\left|u\right\rangle {% endequation %} היא בדיוק מה שתיארנו כרגע. כמובן, בפועל זה בדיוק אותו דבר כמו מה שתיארתי קודם - התיאור עם וקטור שורה הוא פשוט המטריצה המייצגת של {% equation %}f_{v}{% endequation %}. אבל זה לא אומר ששתי דרכי התיאור הקצת שונות הללו לא מסייעות, כל אחת בדרכה, להבין מה הולך פה.

בואו נמשיך עם ההגדרות: במרחב מכפלה פנימית לכל איבר יש <strong>נורמה</strong>, שאפשר לחשוב עליה בתור הגודל שלו: {% equation %}\|v\|\triangleq\sqrt{\left\langle v|v\right\rangle }{% endequation %} . אצלנו ב-{% equation %}\mathbb{C}^{2}{% endequation %} מקבלים {% equation %}\|v\|=\sqrt{\left|a\right|^{2}+\left|b\right|^{2}}{% endequation %}. מה שבדרך כלל אוהבים במתמטיקה הוא איברים מנורמה 1 (שלפעמים נקראים "מנורמלים"), וזה מה שקורה גם בחישוב קוונטי: הערכים שקיוביט יכול לקבל הם <strong>בדיוק</strong> האיברים מנורמה 1 של {% equation %}\mathbb{C}^{2}{% endequation %}. זה נשמע שרירותי, אבל בהמשך נראה שזה נובע מטיעון שקשור להסתברות - ה-1 הזה יהיה סכום של הסתברויות שקשורות לקיוביט (במרחב הסתברות הסכום הכולל של כל ההסתברויות של אירועים מסוימים צריך להיות 1).

במרחב {% equation %}\mathbb{C}^{n}{% endequation %} יש לנו בסיס פשוט במיוחד: <strong>הבסיס הסטנדרטי</strong>, שכולל את כל הוקטורים שהם 1 בכניסה אחת ו-0 באחרות. ב-{% equation %}\mathbb{C}^{2}{% endequation %} אני נותן לו סימון דיראקי פשוט:

{% equation %}\left|0\right\rangle \triangleq\left(\begin{array}{c} 1\\ 0 \end{array}\right){% endequation %} ו-{% equation %}\left|1\right\rangle \triangleq\left(\begin{array}{c} 0\\ 1 \end{array}\right){% endequation %}

לא צריך לייחס ל-0 וה-1 הזה שבתוך הסוגריים יותר מדי משמעות, היה אפשר לשים שם באותה מידה ציור של חתול שמח וחתול כועס. אלו פשוט סימונים סטנדרטיים, ויש גם וקטורים שמסומנים בצורה לא מספרית, למשל {% equation %}\left|+\right\rangle \triangleq\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %} . כשמסתכלים על הוקטור המוזר הזה מייד קופץ לעיניים ה-{% equation %}\sqrt{2}{% endequation %}, למה הוא שם? ובכן, כדי <strong>לנרמל</strong> אותו: אם אני לוקח את הסכום {% equation %}\left|0\right\rangle +\left|1\right\rangle {% endequation %}, מה תהיה הנורמה שלו? זו הזדמנות לעשות חישוב טכני קליל ולראות איך הסימון של דיראק עוזר לנו: אנחנו צריכים לחשב את המכפלה הפנימית של {% equation %}\left|0\right\rangle +\left|1\right\rangle {% endequation %} עם עצמו, ועל פי הסימון של דיראק זה פשוט

{% equation %}\left(\left\langle 0\right|+\left\langle 1\right|\right)\left(\left|0\right\rangle +\left|1\right\rangle \right){% endequation %}

למה? ובכן, כי הפעולה של שחלוף + הצמדה היא <strong>לינארית</strong>, כלומר {% equation %}\left(v+u\right)^{*}=v^{*}+u^{*}{% endequation %} וגם {% equation %}\left(\lambda v\right)^{*}=\overline{\lambda}v^{*}{% endequation %}. לכן הסכום {% equation %}\left|0\right\rangle +\left|1\right\rangle {% endequation %} הופך לסכום {% equation %}\left\langle 0\right|+\left\langle 1\right|{% endequation %}, וגם סקלרים יתהפכו בצורה נחמדה (אבל לא לשכוח להצמיד אותם! אני שכחתי עשרות פעמים וכל פעם זה נקם בי).

עכשיו, את הביטוי {% equation %}\left(\left\langle 0\right|+\left\langle 1\right|\right)\left(\left|0\right\rangle +\left|1\right\rangle \right){% endequation %} אפשר לקרוא בתור הפעלה של אופרטור לינארי על {% equation %}\left(\left|0\right\rangle +\left|1\right\rangle \right){% endequation %} ומכיוון שאופרטור לינארי הוא לינארי הוא מתפרק יפה על פי חוקי הפילוג הרגילים, ואנחנו מקבלים:

{% equation %}\left(\left\langle 0\right|+\left\langle 1\right|\right)\left(\left|0\right\rangle +\left|1\right\rangle \right)=\left\langle 0|0\right\rangle +\left\langle 0|1\right\rangle +\left\langle 1|0\right\rangle +\left\langle 1|1\right\rangle {% endequation %}

זו הסיבה שאנחנו כל כך אוהבים אלגברה לינארית - הכל פשוט מסתדר בה כמו בחשבון פשוט. עכשיו, מה זה {% equation %}\left\langle 0|0\right\rangle {% endequation %}? קל לראות עם חישוב ישיר שזה 1, וש-{% equation %}\left\langle 0|1\right\rangle =\left\langle 1|0\right\rangle =0{% endequation %} וש-{% equation %}\left\langle 1|1\right\rangle =1{% endequation %} גם כן. במילים אחרות, {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} הם בסיס של {% equation %}\mathbb{C}^{2}{% endequation %} שבו כל איבר הוא מנורמה 1, וכל שני איברים שונים הם בעלי מכפלה פנימית 0 ("אורתוגונליים"). לבסיס כזה קוראים <strong>בסיס אורתונורמלי</strong> ואנחנו מאוד אוהבים אותו כי כשעובדים בבסיס אורתונורמלי הכל פתאום פשוט יותר.

ובכן, קיבלנו ש-{% equation %}\left(\left\langle 0\right|+\left\langle 1\right|\right)\left(\left|0\right\rangle +\left|1\right\rangle \right)=2{% endequation %}, כלומר הנורמה של {% equation %}\left|0\right\rangle +\left|1\right\rangle {% endequation %} היא {% equation %}\sqrt{2}{% endequation %}, ולכן אנחנו מחלקים ב-{% equation %}\sqrt{2}{% endequation %} כדי לקבל את האיבר מנורמה 1 שהצגתי קודם, {% equation %}\left|+\right\rangle {% endequation %}. באופן דומה אנחנו מסמנים {% equation %}\left|-\right\rangle =\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}{% endequation %}, ו... זהו, עכשיו אנחנו כבר יודעים די הרבה על חישוב קוונטי!

...למרות שבעצם עוד לא הסברתי כלום.

<h2>מה קורה בחישוב קוונטי?</h2>

בגדול, אפשר לתאר את מה שקורה בחישוב קוונטי בתור תהליך עם שלושה שלבים:

<ol> <li>מאתחלים קיוביט לערך {% equation %}\left|0\right\rangle {% endequation %}.</li>


<li>מפעילים על הקיוביט סדרה של טרנספורמציות לינאריות.</li>


<li>מודדים את הקיוביט והפלט הוא תוצאת המדידה.</li>

</ol>

חישוב קוונטי אמיתי הוא מסובך יותר כי אפשר לדבר על אתחולים לערכים שונים, על מדידות שהן לאו דווקא בסיום, וכמובן - על דברים שמערבים יותר מקיוביט אחד, כי רק כשיש הרבה קיוביטים שמעורבים בחישוב פתאום מתחילים לקרות דברים מופלאים. אבל זו נקודת התחלה לא רעה. את המשמעות של 1 אנחנו כבר יכולים להבין, אבל צריך לדבר עוד על מה קורה ב-2 ו-3.

נתחיל עם 2. מה זו טרנספורמציה לינארית אנחנו כבר יודעים, אבל לא <strong>כל</strong> טרנספורמציה לינארית היא חוקית בהקשר הזה; אמרתי שהערכים שקיוביט יכול לקבל הם רק כאלו מנורמה 1, ולכן אם אני מפעיל טרנספורמציה על קיוביט, היא צריכה להיות כזו שמעבירה וקטור מנורמה 1 לוקטור מנורמה 1. טרנספורמציות כאלו נקראות <strong>אוניטריות</strong>. באופן כללי, טרנספורמציה {% equation %}T:V\to V{% endequation %} היא אוניטרית אם {% equation %}TT^{\dagger}=T^{\dagger}T=I{% endequation %} , כשהסימון {% equation %}T^{\dagger}{% endequation %} מייצג את הצמוד ההרמיטי - השחלוף והצמדה של {% equation %}T{% endequation %} (במתמטיקה בדרך כלל מייצגים זאת בתור {% equation %}T^{*}{% endequation %} אבל אני משתמש בסימון הפיזיקלי שמקובל בחישוב קוונטי). 

למה התכונה הזו מוכיחה שהנורמה משתמרת? ובכן, התכונה הבסיסית (שלא אוכיח) של צמוד הרמיטי של אופרטור כלשהו היא ש-{% equation %}\left\langle Tv|u\right\rangle =\left\langle v|T^{\dagger}u\right\rangle {% endequation %} - אפשר "להעביר צד" את {% equation %}T{% endequation %} כשהיא בתוך מכפלה פנימית, במחיר מעבר לצמוד ההרמיטי. עכשיו נעשה את זה על נורמה:

{% equation %}\|Tv\|=\sqrt{\left\langle Tv,Tv\right\rangle }=\sqrt{\left\langle T^{\dagger}Tv,v\right\rangle }=\sqrt{\left\langle v,v\right\rangle }=\|v\|{% endequation %}

יופי, אז ברור לנו אילו טרנספורמציות <strong>מותר</strong> להפעיל בשלב 2. אבל מה <strong>אפשר בפועל</strong> להפעיל? זה תלוי מאוד בשאלה איך המחשב הקוונטי ממומש - אנחנו לא תופסים טרנספורמציות לינאריות מהאוויר, אלא כל פעולה שאנחנו רוצים להפעיל על קיוביט דורשת הנדסה ותכנון מורכבים, שאני כמובן לא נכנס אליהם כאן. בפועל זה אומר שיש סט של טרנספורמציות "סטנדרטיות" שמזכירים בהקשר הזה, למרות שמחשבים קוונטיים יכולים לבצע גם דברים נוספים אם רוצים. אבל בואו נראה חלק מהדברים הסטנדרטיים (לא את כולם).

קודם ראינו סימונים מיוחדים לשני מצבים קוונטיים: {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}. ה-{% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} הללו היו בסיס ולכן מספיק להגדיר את הפעולה של טרנספורמציה לינארית על שניהם כדי שנדע איך היא פועלת על כל איבר במרחב. אז הנה פעולה פשוטה אחת, שנסמן {% equation %}X{% endequation %}:

{% equation %}X\left|0\right\rangle =\left|1\right\rangle {% endequation %}

{% equation %}X\left|1\right\rangle =\left|0\right\rangle {% endequation %}

זו בעצם פעולת ה-NOT שמוכרת לנו מחישוב קלאסי; אחת משתי הפעולות היחידות שאפשר לבצע על ביט בודד בחישוב רגיל, כשהשניה היא הזהות, לא לעשות כלום. כלומר - מכאן והלאה שאר הפעולות שנראה יהיו משהו "מיוחד", שמתאים להקשר של חישוב קוונטי שבו לא פועלים על ביט אלא על קיוביט; על <strong>סופרפוזיציה</strong>.

קל לחשוב את המטריצה של {% equation %}X{% endequation %}:

{% equation %}X=\left(\begin{array}{cc} 0 & 1\\ 1 & 0 \end{array}\right){% endequation %}

חישוב ישיר גם יראה ש-{% equation %}X{% endequation %} היא אוניטרית, אבל לא צריך חישוב כזה; טרנספורמציה שמעבירה בסיס אורתונורמלי לבסיס אורתונורמלי היא תמיד אוניטרית.

הנה פעולה נוספת שנקראת {% equation %}Z{% endequation %}, שמכניסה לתמונה דבר שלא קיים בחישוב קלאסי - שלוקטורים יכולים להיות <strong>מקדמים</strong>:

{% equation %}Z\left|0\right\rangle =\left|0\right\rangle {% endequation %}

{% equation %}Z\left|1\right\rangle =-\left|1\right\rangle {% endequation %}

{% equation %}Z=\left(\begin{array}{cc} 1 & 0\\ 0 & -1 \end{array}\right){% endequation %}

הפעולה הזו מותירה את {% equation %}\left|0\right\rangle {% endequation %} ללא שינוי, אבל היא הופכת את המקדם של {% equation %}\left|1\right\rangle {% endequation %} לשלילי; המקדם של איבר בהקשר הזה נקרא <strong>הפאזה</strong> שלו (מטעמים פיזיקליים שלא אכנס אליהם), אז בזמן שעל {% equation %}X{% endequation %} אפשר לחשוב בתור "היפוך ביט" על {% equation %}Z{% endequation %} אפשר לחשוב בתור "היפוך פאזה".

קצת קשה לקבל תחושה טובה לגבי איך {% equation %}X,Z{% endequation %} מתנהגים בעולם החדש המופלא שנכנסנו אליו בלי לראות דוגמא קצת יותר רצינית, אז בואו נזכיר שני מצבים קוונטיים אחרים שראינו: {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}. כזכור, ההגדרה שלהם הייתה

{% equation %}\left|+\right\rangle =\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %}

{% equation %}\left|-\right\rangle =\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}{% endequation %}

מה קורה כשאני מפעיל את {% equation %}X{% endequation %} על {% equation %}\left|+\right\rangle {% endequation %}? פשוט מאוד, נשתמש בלינאריות של הטרנספורמציה ונקבל

{% equation %}X\left|+\right\rangle =X\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right)=\frac{X\left|0\right\rangle +X\left|1\right\rangle }{\sqrt{2}}=\frac{\left|1\right\rangle +\left|0\right\rangle }{\sqrt{2}}=\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}=\left|+\right\rangle {% endequation %}

ובמילים אחרות - כלום! לא קורה כלום! ומה אם מפעילים אותו על {% equation %}\left|-\right\rangle {% endequation %}?

{% equation %}X\left|-\right\rangle =X\left(\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}\right)=\frac{X\left|0\right\rangle -X\left|1\right\rangle }{\sqrt{2}}=\frac{\left|1\right\rangle -\left|0\right\rangle }{\sqrt{2}}=-\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}=-\left|-\right\rangle {% endequation %}

כלומר, את {% equation %}\left|-\right\rangle {% endequation %} הוא כופל ב-{% equation %}-1{% endequation %}. או במילים אחרות, על {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %} האופרטור {% equation %}X{% endequation %} מתנהג כמו ש-{% equation %}Z{% endequation %} התנהג על {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}. אז איך {% equation %}Z{% endequation %} יתנהג על {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}? כבר אפשר לנחש שכמו ש-{% equation %}X{% endequation %} התנהג על {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}, כלומר יחליף ביניהם. ואכן:

{% equation %}Z\left|+\right\rangle =Z\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right)=\frac{Z\left|0\right\rangle +Z\left|1\right\rangle }{\sqrt{2}}=\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}=\left|-\right\rangle {% endequation %}

{% equation %}Z\left|-\right\rangle =Z\left(\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}\right)=\frac{Z\left|0\right\rangle -Z\left|1\right\rangle }{\sqrt{2}}=\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}=\left|+\right\rangle {% endequation %}

עכשיו, אחרי שנהננו קצת עם {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %} בואו נשים לב לכך שהם בעצמם בסיס אורתונורמלי (זה חישוב קצר למדי), אז האופרטור שיעביר את הבסיס {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} לבסיס {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %} יהיה אוניטרי. האופרטור הזה חשוב בצורה בלתי רגילה - אולי האופרטור השימושי ביותר בחישוב קוונטי. הוא מסומן ב-{% equation %}H{% endequation %} מלשון "הדאמר" (Hadamard) על שם המתמטיקאי הרלוונטי, ומוגדר כאמור על ידי

{% equation %}H\left|0\right\rangle =\left|+\right\rangle {% endequation %}

{% equation %}H\left|1\right\rangle =\left|-\right\rangle {% endequation %}

או בכתיב יותר מפורש:

{% equation %}H=\frac{1}{\sqrt{2}}\left(\begin{array}{cc} 1 & 1\\ 1 & -1 \end{array}\right){% endequation %}

שימו לב לכך ש-{% equation %}H^{\dagger}=H{% endequation %}, וגם {% equation %}X^{\dagger}=X,Z^{\dagger}=Z{% endequation %}; עוד מעט נראה אופרטור שבו זה לא המצב.

בהערת אגב, התופעה הזו שראינו ש-{% equation %}X,Z{% endequation %} "מחליפים תפקידים" כשעוברים מהבסיס {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} לבסיס {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %} מלמדת אותנו ש-{% equation %}HZH^{\dagger}=X{% endequation %} ו-{% equation %}HXH^{\dagger}=Z{% endequation %}. למה? כי {% equation %}HXH^{\dagger}{% endequation %} הוא שילוב הפעולות "תעבור מהבסיס הראשון לשני, תפעיל את {% equation %}X{% endequation %} על הבסיס השני (עם אותו אפקט של {% equation %}Z{% endequation %}, של השארת איבר בסיס אחד ללא שינוי והכפלת השני במינוס 1) ואז תחזור לבסיס המקורי. נסו לחשב ותראו מה קורה. השוויון הזה לא חשוב לנו עכשיו אבל הוא הולך לחזור בהמשך; מילולית אני קורא לפעולה של כפל משמאל באופרטור ומימין בצמוד ההרמיטי שלו בשם <strong>הצמדה</strong>: {% equation %}HXH^{\dagger}{% endequation %} זו ההצמדה של {% equation %}X{% endequation %} על ידי {% equation %}H{% endequation %} (גם פה אני קצת חורג מהקונבנציה המתמטית, שבה הצמוד ההרמיטי יהיה דווקא משמאל ולא מימין).

בואו נראה עוד כמה אופרטורים נפוצים ומועילים. ראשית, {% equation %}Z{% endequation %} בבסיס הסטנדרטי מיוצג על ידי מטריצה <strong>אלכסונית</strong>. מה שנחמד במטריצות כאלו הוא שקל להוציא להן שורש - מוציאים שורש לכל איבר על האלכסון. כלומר, אפשר לכתוב

{% equation %}\sqrt{Z}=\left(\begin{array}{cc} 1 & 0\\ 0 & \pm i \end{array}\right){% endequation %}

נבחר את אחד מהשורשים הללו באופן שרירותי וניתן לו אות משלו:

{% equation %}S=\left(\begin{array}{cc} 1 & 0\\ 0 & i \end{array}\right){% endequation %}

עכשיו מתקיים {% equation %}S^{2}=Z{% endequation %}, וגם קל לראות שהשורש השני הוא פשוט {% equation %}S^{3}{% endequation %}, שהוא גם {% equation %}S^{\dagger}{% endequation %}. קיבלנו עוד אחד מהאופרטורים המרכזיים שלנו.

מה קורה כשמצמידים את {% equation %}X,Z{% endequation %} שלנו בעזרת {% equation %}S{% endequation %}? ובכן, {% equation %}Z{% endequation %} הוא חזקה של {% equation %}S{% endequation %} ולכן מתחלף איתו בכפל, כך שהצמדה לא עושה כלום: {% equation %}SZS^{\dagger}=Z{% endequation %}. אבל לעומת זאת, אם נחשב את {% equation %}SXS^{\dagger}{% endequation %}, נקבל מטריצה שטרם ראינו, ויש לה סימון משל עצמה - {% equation %}Y{% endequation %}:

{% equation %}Y=\left(\begin{array}{cc} 0 & -i\\ i & 0 \end{array}\right){% endequation %}

{% equation %}Y{% endequation %} הוא מין שילוב של הפעולות של {% equation %}X{% endequation %} (מחליף בין {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %}) ושל {% equation %}Z{% endequation %} (כופל ב-{% equation %}-1{% endequation %} את {% equation %}\left|1\right\rangle {% endequation %} לפני ההחלפה), ובתור בונוס הוא גם מכפיל הכל ב-{% equation %}i{% endequation %}. הוא גם הדוגמא האחרונה שרציתי להראות בינתיים. ראינו את האופרטורים {% equation %}X,Y,Z,H,S{% endequation %} שהם התחלה יפה אם כי אני מזהיר מראש שהם לא מספרים את כל הסיפור אפילו עבור קיוביט בודד.

<h2>מדידות</h2>

נעבור עכשיו לשלב 3: מדידה. כדי להסביר מה הולך בשלב הזה צריך לעזוב לרגע את האבסטרקציה ולחזור אל מה שקורה בפיזיקה. כשיש לנו מצב קוונטי בסופרפוזיציה, {% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %}, אנחנו לא יודעים "לקרוא" מתוכו את הערכים {% equation %}\alpha,\beta{% endequation %}. זאת בניגוד לביט רגיל, שאנחנו יכולים לבדוק אם ערכו הוא 0 או 1. מה שכן אפשר לעשות עם המצב הקוונטי {% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %}, מלבד הפעלת טרנספורמציה לינארית שתשנה את המצב הזה למצב אחר אבל לא תיתן לנו אינפורמציה "החוצה", הוא לבצע איתו אינטראקציה שנקראת <strong>מדידה</strong> שעושה שני דברים:

<ol> <li>מחזירה ערך שהוא או 0 או 1 באופן הסתברותי: {% equation %}0{% endequation %} בהסתברות {% equation %}\left|\alpha\right|^{2}{% endequation %} ו-{% equation %}1{% endequation %} בהסתברות {% equation %}\left|\beta\right|^{2}{% endequation %}.</li>


<li>אם הערך שהוחזר היה 0, מעבירה את המצב הקוונטי למצב {% equation %}\left|0\right\rangle {% endequation %}, ואם הערך שהוחזר היה 1 מעבירה אותו למצב {% equation %}\left|1\right\rangle {% endequation %}.</li>

</ol>

שימו לב שהפעולה הזו <strong>אינה</strong> טרנספורמציה אוניטרית, לכן היא לא עוד מקרה של הפעולות משלב 2. בפרט, זו לא פעולה <strong>הפיכה</strong>; אם ביצענו מדידה ועברנו ל-{% equation %}\left|0\right\rangle {% endequation %} או {% equation %}\left|1\right\rangle {% endequation %}, אין לנו דרך לחזור למצב {% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %} המקורי; המקדמים {% equation %}\alpha,\beta{% endequation %} "נהרסו" ואבדו. כל האפקט שלהם התבטא ב<strong>הסתברות</strong> שנקבל 0 או 1. הקושי הזה לקבל החוצה מידע מועיל מתוך הסופרפוזיציה שהגענו אליה הוא המכשול העיקרי שעומד בפני חישוב קוונטי: מצד אחד עוד נראה שאפשר לעשות ניסים ונפלאות בחישוב קוונטי, אבל אחרי שהניסים והנפלאות הללו התרחשו קשה לנו מאוד לחלץ מהם אינפורמציה מועילה, ואלגוריתמים קוונטיים בנויים לרוב מתוך מטרה להגדיל את הסיכוי לקבל את האינפורמציה המועילה הזו בשלב המדידה (וזה כמובן שונה מאוד מהאינטואיציה הרגילה שלנו לגבי איך פועלים חישובים, כי בחישובים שאנחנו מכירים פשוט קוראים את הביטים ורואים מה יש בהם).

בואו נראה דוגמאות. ראשית, אם מודדים את {% equation %}\left|0\right\rangle {% endequation %} נקבל את התוצאה 0 בהסתברות 1, כי אם אני כותב את {% equation %}\left|0\right\rangle {% endequation %} באופן כללי בתור {% equation %}\left|0\right\rangle =\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %} אז {% equation %}\alpha=1,\beta=0{% endequation %} ולכן ההסתברות לקבל 0 היא {% equation %}\left|1\right|^{2}=1{% endequation %}. בדומה מדידה של {% equation %}\left|1\right\rangle {% endequation %} תחזיר 1 בהסתברות 1.

לעומת זאת, מדידה של {% equation %}\left|+\right\rangle =\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %} היא קצת יותר מעניינת: אם נכתוב {% equation %}\left|+\right\rangle =\frac{1}{\sqrt{2}}\left|0\right\rangle +\frac{1}{\sqrt{2}}\left|1\right\rangle {% endequation %} יהיה לנו קצת יותר קל לראות שכאן {% equation %}\alpha=\beta=\frac{1}{\sqrt{2}}{% endequation %} ולכן {% equation %}\left|\alpha\right|^{2}=\left|\beta\right|^{2}=\frac{1}{2}{% endequation %}, כלומר זה מצב שכשמודדים אותו מקבלים 0 בהסתברות חצי ו-1 בהסתברות חצי. עבור {% equation %}\left|-\right\rangle {% endequation %} קורה אותו דבר בדיוק, כי {% equation %}\left|-\right\rangle =\frac{1}{\sqrt{2}}\left|0\right\rangle -\frac{1}{\sqrt{2}}\left|1\right\rangle {% endequation %} ולכן כאן {% equation %}\alpha=\frac{1}{\sqrt{2}},\beta=-\frac{1}{\sqrt{2}}{% endequation %}, והסימן השונה הולך לאיבוד כשלוקחים ערך מוחלט ומעלים בריבוע ומקבלים שוב {% equation %}\left|\alpha\right|^{2}=\left|\beta\right|^{2}=\frac{1}{2}{% endequation %}.

כבר עכשיו ראינו מספיק כדי לשבור מיסקונספציה נפוצה שעלולה לצוץ בתיאורים פופולריים של חישוב קוונטי. לפעמים מתארים מצב קוונטי בתור משהו שמערב הסתברויות ותו לא. חיפוש מהר בגוגל העלה (לא משנה מאיזה אתר) את הטקסט הבא על קיוביט: "על מנת לממש אותו יש צורך למצוא מערכת פיזיקלית שאפשר לשלוט ביעילות במצב הקוונטי שלה ולהקנות לה ערך מסוים של 0 או 1, או הסתברות כלשהי למדוד אותה באחד מהם." אף אחד לא יקרא את התיאורים הפופולריים הללו ונפשו הרכה תינזק או שיכולתו להבין חישוב קוונטי תיפגע לצמיתות, אבל הם לא מספרים את הסיפור האמיתי; בשביל "סתם" הסתברויות לא צריך חישוב קוונטי, מספיק חישוב הסתברותי רגיל, אבל חישוב קוונטי מוסיף לנו רמה של תחכום מתמטי שפשוט לא ניתן לקבל בחישוב הסתברותי רגיל.

הנה ההמחשה הפשוטה לכך: נניח שיש לנו מערכת שהיא או במצב {% equation %}\left|+\right\rangle {% endequation %} או במצב {% equation %}\left|-\right\rangle {% endequation %}, אנחנו לא יודעים איזה. אם נמדוד אותה, נקבל {% equation %}0{% endequation %} או 1 בהסתברות חצי-חצי. אם יש לנו 1,000 עותקים של המערכת הזו נוכל למדוד אותה 1,000 פעמים ולקבל התפלגות תוצאות שהיא בערך חצי-חצי, כך שנוכל להסיק שההסתברויות הן חצי-חצי. האם זה מספר לנו את כל הסיפור על המערכת? לחלוטין לא. כי אם ניקח את המערכת ולפני שנמדוד אותה נפעיל עליה {% equation %}H{% endequation %}, הסיטואציה תשתנה דרסטית; או שתמיד נמדוד 0, אם המצב המקורי היה {% equation %}\left|+\right\rangle {% endequation %}, או שתמיד נמדוד 1 אם המצב המקורי היה {% equation %}\left|-\right\rangle {% endequation %}. כלומר, המצב הקוונטי הוא יותר מ"סתם" הסתברויות - יש למקדמים חשיבות, וגם אם החשיבות הזו לא באה לידי ביטוי באופן ישיר במדידה, היא יכולה לבוא לידי ביטוי אם נבצע עוד פעולות על המצב הקוונטי לפני המדידה.

מושג ה"מדידה" שהצגתי כאן הוא מקרה פרטי של כל המדידות שאפשר לבצע; אני לא אציג עדיין את ההגדרה המלאה (אבל היא תבוא), אבל הנה קצת גיוון: מכיוון ש-{% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %} גם הוא בסיס אורתונורמלי, בהינתן מצב קוונטי כללי, שאני מסמן {% equation %}\left|\psi\right\rangle {% endequation %}, אפשר לכתוב גם {% equation %}\left|\psi\right\rangle =\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %} אבל גם לכתוב {% equation %}\left|\psi\right\rangle =\gamma\left|+\right\rangle +\delta\left|-\right\rangle {% endequation %}. עכשיו, מכיוון ש-{% equation %}\left|\psi\right\rangle {% endequation %} הוא מצב קוונטי הוא מנורמה 1, כלומר מתקיים {% equation %}\left|\alpha\right|^{2}+\left|\beta\right|^{2}=1{% endequation %} וגם מתקיים {% equation %}\left|\gamma\right|^{2}+\left|\delta\right|^{2}=1{% endequation %}, כלומר אפשר לחשוב על {% equation %}\left|\alpha\right|^{2},\left|\beta\right|^{2}{% endequation %} כמייצגים הסתברות - ההסתברות שמדידה תניב לנו 0 או 1 - ואפשר גם לחשוב על {% equation %}\left|\gamma\right|^{2},\left|\delta\right|^{2}{% endequation %} כמייצגים הסתברות, של מדידה <strong>שונה</strong>, מדידה על פי הבסיס {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %}. מדידה כזו תחזיר ערך {% equation %}+{% endequation %} בהסתברות {% equation %}\left|\gamma\right|^{2}{% endequation %} וערך {% equation %}-{% endequation %} בהסתברות {% equation %}\left|\delta\right|^{2}{% endequation %} ותעביר את המערכת למצב המתאים, {% equation %}\left|+\right\rangle {% endequation %} או {% equation %}\left|-\right\rangle {% endequation %}.

זה נשמע קצת מוזר. מה זה אומר "להחזיר {% equation %}+{% endequation %}"? ובכן, הרעיון במדידה הוא לא בהכרח הערך המספרי הקונקרטי שאני מקבל, אלא מה שהוא <strong>מייצג</strong>. כאן אני משתמש בסימן {% equation %}+{% endequation %} כדי לתאר "תוצאת המדידה שמתאימה לכך שהמצב {% equation %}\left|+\right\rangle {% endequation %} 'ניצח' בהגרלה". איך זה בא לידי ביטוי במציאות? זה תלוי באופן המדויק שבו מבצעים מדידה, אבל שווה לזכור שזה כך כבר כשמדברים על ביטים רגילים: כשאני "מודד" ביט רגיל אני מגלה שהוא נמצא ברמת מתח כלשהי, נאמר 563 (אני לא מכניס יחידות בכוונה, מה אני מבין בזה בכלל?) ובמדידה אחרת הוא בכלל ברמת מתח 13. אני קובע, מתוך ידיעה עם איך שההתקן הפיזי עובד, שכל מדידה שמחזירה רמת מתח בין 10 ל-100 היא "0" וכל מדידה שמחזירה משהו בין 500 ל-600 היא "1"; ביצעתי כאן אבסטרקציה של הערך הפיזי שמדדתי. זה מה שקורה גם בחישוב קוונטי, אם כי יש פורמליזם מתמטי יפה שגורם לתוצאות המדידה להיראות קצת פחות שרירותיות ואראה אותו בהמשך (בפורמליזם הזה גם מדידה בבסיס {% equation %}\left|0\right\rangle ,\left|1\right\rangle {% endequation %} וגם מדידה בבסיס {% equation %}\left|+\right\rangle ,\left|-\right\rangle {% endequation %} מחזירות את הערכים {% equation %}\pm1{% endequation %}).

<h2>סיכום ביניים קצר</h2>

יפה, אז מה ראינו? ראינו שיחידת המידע הבסיסית בחישוב קוונטי היא קיוביט, ושהערך שלו מיוצג על ידי איבר של {% equation %}\mathbb{C}^{2}{% endequation %} מנורמה 1; ראינו שאפשר לפעול על קיוביט על ידי הפעלה של אופרטור אוניטרי ושדוגמאות פופולריות לאופרטורים כאלו הן {% equation %}X,Y,Z,H,S{% endequation %}; וראינו שאפשר למדוד קיוביט בצורה שנותנת לנו אינפורמציה ומשנה את מצב הקיוביט בהתאם לתוצאת המדידה. אלו הרכיבים הבסיסיים של חישוב קוונטי, אבל בשלב הזה ייתכן שיש לכם הרגשה שמשהו חסר, ובצדק.

כי מה היה לנו עד כה? כדי לתאר מצב קוונטי כללי {% equation %}\left|\psi\right\rangle =\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %} אני בסך הכל צריך וקטור מאורך 2 של מספרים מרוכבים, {% equation %}\left(\begin{array}{c} \alpha\\ \beta \end{array}\right){% endequation %}. להפעיל אופרטור אוניטרי על וקטור כזה הוא בסך הכל כפל במטריצה {% equation %}2\times2{% endequation %}, וביצוע מדידה הוא בסך הכל חישוב {% equation %}\left|\alpha\right|^{2},\left|\beta\right|^{2}{% endequation %} והגרלת מספר בין 0 ו-1. את כל הדברים הללו <strong>קל מאוד </strong>לבצע במחשב רגיל; אין סיבה לבנות מחשב קוונטי במיוחד בשביל זה.

הכוח האמיתי של חישוב קוונטי מגיע רק כאשר אנחנו עובדים עם מערכות שמורכבות מיותר מקיוביט אחד. כבר כשיש לנו 50 קיוביטים בערך אנחנו מתקרבים לקצה גבול היכולת של מה שמחשבים רגילים יכולים "לסמלץ" בצורה מלאה, ועל 100 קיוביטים אין מה לדבר. לכן זה הדבר הבא שאני צריך להציג: איך אני מתאר מבחינה מתמטית מערכות שמורכבות ממספר גדול מ-1 של קיוביטים, ואיך נראים חישובים בהן? את זה אעשה בפוסט הבא. 