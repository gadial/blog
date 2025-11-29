---
id: 2182
title: "משפט השאריות הסיני"
date: 2012-09-12 18:18:18
layout: post
categories: 
  - אלגברה מופשטת
  - תורת המספרים
tags: 
  - משפט השאריות הסיני
social_media_share: true
---
בית הספר "הר סיני" החליט להתעלל בשכבת כיתה י' שלו ולארגן מהם קבוצות למשחק כדור זה או אחר. ראשית לקח בית הספר את כלל תלמידי השכבה והחל לחלק אותם לקבוצות כדורגל (11 שחקנים בקבוצה) אבל לרוע המזל התברר שנותר תלמיד אחד בלי קבוצה. טוב, אז בית הספר מיהר לחלק אותם לקבוצות כדורסל (5 שחקנים בקבוצה), אבל שוב נותר בחוץ תלמיד אחד. טוב, אז בית הספר ניסה עכשיו לחלק אותם לקבוצות בייסבול (9 שחקנים בקבוצה), אבל <strong>שוב</strong> נשאר בחוץ בדיוק תלמיד אחד. ידוע שיש בשכבה לא יותר מ-1000 תלמידים, ומספר התלמידים הוא זוגי - כמה תלמידים יש בשכבה?

את החידה המטופשת הזו המצאתי כרגע, בלי לבצע חישובים כמעט בכלל. זה מעניין, כי יש יומרנות כלשהי בכך שאני מציג אותה - אני בעצם טוען שלחידה הזו <strong>יש פתרון</strong>, למרות שאני עצמי לא יודע מהו כרגע. אם כן, מהו הפתרון? איך מוצאים אותו? מדוע מובטח שהוא קיים? אלו השאלות שעליהן עונה <strong>משפט השאריות הסיני</strong>.

לפני שנגיע אליו, בואו ננסה לפתור את החידה בצורה נאיבית. לצורך העניין נסמן את מספר התלמידים בשכבה ב-{% equation %}x{% endequation %}. כעת, אמרו לנו שכאשר מנסים לחלק את {% equation %}x{% endequation %} ב-11, נשארים עם שארית 1. במתמטיקה יש סימון קומפקטי שבא לתאר את התופעה הזו: {% equation %}x\equiv1\left(\text{mod 11}\right){% endequation %}, שיש לקרוא כ"{% equation %}x{% endequation %} שקול ל-1 מודולו 11". באופן כללי, {% equation %}a\equiv b\left(\text{mod }n\right){% endequation %} פירושו שהשארית שמקבלים כאשר מחלקים את {% equation %}a{% endequation %} ב-{% equation %}n{% endequation %} שווה לשארית שמקבלים כשמחלקים את {% equation %}b{% endequation %} ב-{% equation %}n{% endequation %} (למשל, {% equation %}13\equiv31\left(\text{mod 6}\right){% endequation %}). אפשר לראות בלי יותר מדי עבודה שהטענה "{% equation %}a{% endequation %} ו-{% equation %}b{% endequation %} מחזירים אותה שארית בחלוקה ב-{% equation %}n{% endequation %}" שקולה לטענה "{% equation %}a-b{% endequation %} מתחלק ב-{% equation %}n{% endequation %}" ולרוב את התנאי השני קל יותר לבדוק (וזו גם ההגדרה היותר מקובלת של הסימון של שקילות מודולו).

אני עצל למדי ולכן במקום לכתוב {% equation %}x\equiv1\left(\text{mod 11}\right){% endequation %} (מה שהוא, כאמור, הסימון הסטנדרטי) אכתוב {% equation %}x\equiv_{11}1{% endequation %} (שהוא פחות סטנדרטי אבל פה ושם משתמשים בו) ובאופן כללי אכתוב {% equation %}a\equiv_{n}b{% endequation %} ואסמוך עליכם שתבינו למה אני מתכוון.

תכונה חשובה ביותר של משוואות מודולריות, שאשתמש בה הרבה בהמשך, היא שחוקי החיבור והכפל מתקיימים עבורן. כלומר, אם {% equation %}a\equiv_{n}x{% endequation %} ו-{% equation %}b\equiv_{n}y{% endequation %} אז
<ol>
	<li>{% equation %}a+b\equiv_{n}x+y{% endequation %}</li>
	<li>{% equation %}a\cdot b\equiv_{n}x\cdot y{% endequation %}</li>
</ol>
זה תרגיל נחמד להוכיח את הטענות הללו (עבור 2 צריך לחשוב טיפה). נסו לעשות זאת! (המשוואות נכונות גם עבור מספר סופי כלשהו של מחוברים - את זה מוכיחים באינדוקציה).

כעת אפשר לנסח את החידה שלעיל בלשון קצת יותר מתמטית: מהו {% equation %}1\le x\le1000{% endequation %} המקיים:

{% equation %}x\equiv_{11}1{% endequation %}

{% equation %}x\equiv_{5}1{% endequation %}

{% equation %}x\equiv_{9}1{% endequation %}

{% equation %}x\equiv_{2}0{% endequation %} (זו בעצם הדרישה "מספר התלמידים זוגי" - שהכנסתי כדי למנוע את הפתרון המטופש של "בשכבה יש תלמיד אחד").

וכמובן, איך למצוא אותו?

במילים אחרות, מבקשים מאיתנו לפתור <strong>מערכת משוואות מודולריות</strong>. למצוא {% equation %}x{% endequation %} שפותר את כל המשוואות "בו זמנית", אם קיים כזה. איך עושים את זה?

הדרך הנאיבית היא זו: אם {% equation %}x\equiv_{11}1{% endequation %} זה אומר ש-{% equation %}x{% endequation %} יכול להיות אחד מבין המספרים הבאים: {% equation %}1,12,23,34,\dots{% endequation %} - הבנתם את הרעיון, מתחילים מ-1 ובכל פעם מוסיפים 11. כעת, אם {% equation %}x\equiv_{5}1{% endequation %} הוא יכול להיות אחד מבין המספרים הבאים: {% equation %}1,6,11,16,\dots{% endequation %} וכן הלאה. בסופו של דבר נקבל ארבע קבוצות של מספרים, אחת לכל משוואה; ואז כל מה שצריך לעשות יהיה לחפש איבר שמופיע בכולן בו זמנית. רק מה, חיפוש כזה הוא דבר לא יעיל במיוחד. אפילו מאוד לא יעיל, ואילו אנחנו רוצים פתרון שהוא <strong>מהיר</strong>. זה אולי לא נראה כך כרגע, אבל פתרון משוואות מודולריות שכאלו הוא הלחם והחמאה של תורת המספרים האלגוריתמית, במובן זה שצריך לפתור משוואות מודולריות לעתים קרובות <strong>כחלק</strong> מאלגוריתם מסובך יותר.

אציג את מה שמשפט השאריות הסיני עושה קודם כל עבור המקרה הפרטי של החידה שלנו, ואז נראה איך זה מוכלל לפתרון של כל מערכת משוואות מודולרית. הרעיון הבסיסי הוא זה: נניח שהצלחתי באופן קסום כלשהו למצוא ארבעה מספרים {% equation %}a,b,c,d{% endequation %} שמקיימים את התכונות הבאות:
<ol>
	<li>{% equation %}a\equiv_{11}1{% endequation %} וכמו כן {% equation %}a{% endequation %} מתחלק ב-{% equation %}5,9,2{% endequation %}.</li>
	<li>{% equation %}b\equiv_{5}1{% endequation %} וכמו כן {% equation %}b{% endequation %} מתחלק ב-{% equation %}11,9,2{% endequation %}.</li>
	<li>{% equation %}c\equiv_{9}1{% endequation %} וכמו כן {% equation %}c{% endequation %} מתחלק ב-{% equation %}11,5,2{% endequation %}.</li>
	<li>{% equation %}d\equiv_{2}0{% endequation %} וכמו כן {% equation %}d{% endequation %} מתחלק ב-{% equation %}11,5,9{% endequation %} (ההפרדה כאן בין 2 ושאר המספרים אולי נראית מלאכותית אבל יש לה מטרה).</li>
</ol>
אני טוען שאם מצאתי את המספרים הללו, כמעט סיימתי: אני אגדיר {% equation %}x=a+b+c+d{% endequation %} ואקבל מספר שמקיים את כל ארבעת המשוואות המודולריות שלעיל. למה? כי בואו נשאל את עצמו, למשל, מהו {% equation %}x{% endequation %} מודולו 11. על פי חוקי החשבון המודולרי:

{% equation %}x\equiv_{11}a+b+c+d\equiv_{11}1+0+0+0\equiv_{11}1{% endequation %}

מה בעצם קרה כשלקחנו את המשוואה מודולו 11? הגורמים של {% equation %}b,c,d{% endequation %} התפוגגו ואינם עוד, כי כולם התחלקו ב-11. האיבר היחיד שלא התחלק ב-11 היה {% equation %}a{% endequation %}, ועבורו ידענו ספציפית שהוא מחזיר 1 מודולו 11. באותו האופן נקבל את התוצאה שאנחנו רוצים גם כשניקח את {% equation %}x{% endequation %} מודולו {% equation %}5,9{% endequation %} או 2.

האם סיימנו? לא בהכרח, כי ייתכן ש-{% equation %}x{% endequation %} יהיה גדול מ-1000. במקרה הזה פשוט נחלק אותו ב-{% equation %}11\cdot5\cdot9\cdot2=990{% endequation %} וניקח את השארית (שתהיה מספר בין 1 ל-990). למה זה עובד? ובכן, כי אם {% equation %}x\equiv_{990}y{% endequation %}, אז בפרט גם {% equation %}x\equiv_{11}y{% endequation %} וכך גם עבור {% equation %}5,9,2{% endequation %}. למה? באופן כללי, אם {% equation %}x\equiv_{n}y{% endequation %}, ויש לנו מספר {% equation %}k{% endequation %} שמחלק את {% equation %}n{% endequation %}, אז מכיוון ש-{% equation %}n{% endequation %} מחלק את {% equation %}x-y{% endequation %} גם {% equation %}k{% endequation %} מחלק את {% equation %}x-y{% endequation %} (חלוקה היא יחס <strong>טרנזיטיבי</strong>). למי שחייב לראות את זה בעיניים הנה הוכחה קונקרטית: אם {% equation %}n{% endequation %} מחלק את {% equation %}x-y{% endequation %} זה אומר ש-{% equation %}x-y=\alpha\cdot n{% endequation %}. עבור {% equation %}\alpha{% endequation %} שלם כלשהו. אם {% equation %}k{% endequation %} מחלק את {% equation %}n{% endequation %} זה אומר ש-{% equation %}n=k\beta{% endequation %} עבור {% equation %}\beta{% endequation %} שלם כלשהו. על כן, {% equation %}x-y=\alpha\cdot\beta\cdot k{% endequation %} ולכן {% equation %}k{% endequation %} מחלק את {% equation %}x-y{% endequation %}.

יפה, אם כן, סיימנו לפתור את החידה, פרט לכך שעדיין אין לנו מושג איך למצוא את {% equation %}a,b,c,d{% endequation %} המדוברים.

עכשיו אני אעשה להטוט קטן שמטרתו למצוא את {% equation %}a{% endequation %}. ייתכן שלא תבינו מאיפה הלהטוט הזה מגיע, ובצדק; זה לב-לבו של הרעיון של משפט השאריות הסיני. העיקר כאן הוא להבין <strong>למה</strong> הלהטוט עובד.

אני לוקח את 990 - המכפלה של ארבעת המספרים שמשתתפים במשוואות המודולריות בתור "מה שמחלקים בו" - מה שאקרא לו מעכשיו <strong>המודולוסים</strong>. אני רוצה למצוא את {% equation %}a{% endequation %} ש"עובד" עבור המודולוס 11; אני אתחיל בכך שאחלק את 990 ב-11 ואקבל 90. כעת, 90 ו-11 הם <strong>מספרים זרים</strong>, כלומר אין להם אף מחלק משותף; זה מבטיח שאפשר למצוא מספר {% equation %}y{% endequation %} בעל התכונה {% equation %}90\cdot y\equiv_{11}1{% endequation %}. איך מוצאים כזה? בהמשך. לעת עתה אגלה לכם שבמקרה שלנו, {% equation %}y=6{% endequation %}. אם כן, מהו {% equation %}90\cdot y{% endequation %}? חישוב קצר מראה לנו שזהו {% equation %}540=49\cdot11+1{% endequation %}. אני טוען שאם כן, {% equation %}a=540{% endequation %} הוא המספר שאנחנו מחפשים. ראינו לפני רגע שהוא מקיים {% equation %}540\equiv_{11}1{% endequation %}. למה הוא מתחלק ב-{% equation %}5,9,2{% endequation %}? ובכן, כי הגדרנו אותו בתור מכפלה של 90 בעוד משהו, ו-90 הוא בדיוק המכפלה של {% equation %}5,9,2{% endequation %} ולכן ברור שמתחלק בכולם.

באותו האופן נטפל גם ב-{% equation %}b{% endequation %}: נתחיל מ-990, נחלק אותו ב-5, נקבל 198, נשים לב לכך ש-{% equation %}396=198\cdot2{% endequation %} מחזיר שארית 1 בחלוקה ב-5, ולכן {% equation %}b=396{% endequation %} הוא המספר שאנחנו רוצים. גם {% equation %}c{% endequation %} מטופל באותו האופן: מתחילים מ-990, מחלקים ב-9, מקבלים 110, שמים לב לכך ש-{% equation %}550=110\cdot5{% endequation %} מחזיר שארית 1 בחלוקה ב-9 ולכן {% equation %}c=550{% endequation %}.

ומה עם {% equation %}d{% endequation %}? כמקודם, 990 חלקי 2 זה 495, אבל הפעם אנחנו רוצים לא 1 מודולו 2 אלא 0. טוב, אז כאן אפשר "לרמות" ופשוט לבחור {% equation %}d=0{% endequation %}. בהמשך נראה שזו לא באמת רמאות אלא מה שבכל מקרה אמורים לעשות.

בסך הכל נקבל {% equation %}x=540+396+550+0=1486{% endequation %}. זה יצא גדול יותר מ-990, אז כאמור - מחלקים ב-990 ולוקחים את השארית, כלומר {% equation %}x=496{% endequation %} הוא הפתרון שאנחנו מחפשים. אתם מוזמנים לעשות את החישוב ולראות שזה עובד.

בואו נסבך קצת את החידה. נניח שהיינו רוצים שישאר לא ילד אחד מודולו 11, אלא <strong>בדיוק</strong> שבעה? איך הפתרון היה משתנה אז? ובכן, לא בהרבה: {% equation %}b,c,d{% endequation %} שלנו הם עדיין בסדר. רק צריך למצוא {% equation %}a{% endequation %} כך ש-{% equation %}a\equiv_{11}7{% endequation %} ועדיין מתחלק ב-2,9,5.

עכשיו, ראינו כבר ש-{% equation %}540\equiv_{11}1{% endequation %}. לכן, אם נכפול את שני האגפים ב-7, נקבל {% equation %}540\cdot7\equiv_{11}7{% endequation %}, וברור ש-{% equation %}540\cdot7{% endequation %} מתחלק ב-{% equation %}5,9,2{% endequation %} (כי 540 התחלק בהם). לכן {% equation %}a=540\cdot7=3780{% endequation %} הוא המספר שאנו רוצים. נקבל ש-{% equation %}a+b+c+d=4726{% endequation %}, ואחרי חלוקה ב-990 והוצאת שארית נקבל 766 תלמידים בשכבה. אתם מוזמנים לבדוק שהמספר הזה עובד טוב.

יפה. סיימנו עם הדוגמה, ואני רוצה לעבור למקרה הכללי. עם זאת, לפני כן אני רוצה לתת דוגמה אחרת שממחישה ש<strong>לא תמיד</strong> יש פתרון לכל מערכת משוואות מודולרית. הנה מערכת כזו לדוגמה:

{% equation %}x\equiv_{4}3{% endequation %}

{% equation %}x\equiv_{8}6{% endequation %}

למערכת הזו אין שום סיכוי שיהיה פתרון. למה? כי אם {% equation %}x-6{% endequation %} מתחלק ב-8, אז הוא בפרט מתחלק ב-4, כלומר {% equation %}x\equiv_{4}6\equiv_{4}2{% endequation %}, אבל זה עומד בסתירה לכך ש-{% equation %}x\equiv_{4}3{% endequation %} - הרי איקס לא יכול להחזיר גם שארית 2 וגם שארית 3 בחלוקה ב-4!

התחושה היא שהבעיה במערכת הזו היא ששתי המשוואות היו <strong>תלויות זו בזו</strong> במידה מסויימת בגלל ש-4 חילק את 8. אולי אם נאסור על אחד מהמודולוסים לחלק את השני לא יהיו לנו בעיות? לרוע המזל לא, כפי שמראה הדוגמה הבאה:

{% equation %}x\equiv_{6}3{% endequation %}

{% equation %}x\equiv_{15}7{% endequation %}

כאן המודולוסים בוודאי לא מחלקים אחד את השני. מצד שני, 3 מחלק את שניהם! המשוואה הראשונה גוררת ש-{% equation %}x\equiv_{3}0{% endequation %} והשני גוררת ש-{% equation %}x\equiv_{3}1{% endequation %}, ושוב קיבלנו סתירה. במילים אחרות, עלולה להיות לנו בעיה אם יש שני מודולוסים שיש מספר שמחלק את שניהם גם יחד. מספרים שלמים שהמספר הגדול ביותר שמחלק את שניהם גם יחד הוא 1 נקראים <strong>זרים</strong>; התקווה היא שאם כל המודולוסים הם זרים זה לזה (כלומר, לכל זוג מודולוסים, אין לו מחלק משותף שגדול מ-1) אז כל מערכת משוואות עם אותם מודולוסים תהיה פתירה. התקווה הזו התגשמה: בואו ננסח את משפט השאריות הסיני באופן מדויק.

אם כן, יהיו מספרים שלמים {% equation %}m_{1},m_{2},\dots,m_{k}{% endequation %} שכולם זרים בזוגות (לכל זוג {% equation %}m_{i},m_{j}{% endequation %}, המחלק המשותף הגדול ביותר שלהם הוא 1). בנוסף, יהיו גם מספרים שלמים {% equation %}a_{1},\dots,a_{k}{% endequation %} <strong>כלשהם</strong>. נסמן {% equation %}m=m_{1}m_{2}\cdots m_{k}{% endequation %} (המכפלה של כל המודולסים). אז משפט השאריות הסיני אומר שלמערכת המשוואות הבאה:

{% equation %}x\equiv_{m_{1}}a_{1}{% endequation %}

{% equation %}\vdots{% endequation %}

{% equation %}x\equiv_{m_{k}}a_{k}{% endequation %}

יש פתרון בתחום {% equation %}0\le x<m{% endequation %} והפתרון הזה הוא <strong>יחיד</strong> בתחום הזה (ולכן קבוצת כל הפתרונות למשוואה היא הקבוצה {% equation %}\left\{ x+tm\ |\ t\in\mathbb{Z}\right\} {% endequation %}, אבל זה פחות חשוב).

ההוכחה של המשפט הכללי דומה לפתרון של המקרה הפרטי. קודם כל נוכיח שבכלל יש פתרון, כי זה העיקר. לכל {% equation %}i{% endequation %}, נגדיר {% equation %}n_{i}=\frac{m}{m_{i}}{% endequation %}, כלומר המכפלה של כל המודולוסים חוץ מ-{% equation %}m_{i}{% endequation %}. כעת, {% equation %}m_{i}{% endequation %} ו-{% equation %}n_{i}{% endequation %} הם זרים (כי {% equation %}m_{i}{% endequation %} זר לכל הגורמים של {% equation %}n_{i}{% endequation %}). מכאן נובע (לזה אתייחס בהמשך) שקיים מספר {% equation %}d_{i}{% endequation %} כך ש-{% equation %}n_{i}d_{i}\equiv_{m_{i}}1{% endequation %}. בואו לצורך נוחות בלבד נסמן {% equation %}e_{i}=n_{i}d_{i}{% endequation %}. שימו לב ש-{% equation %}e_{i}{% endequation %} מקיים את התכונה הבאה:

{% equation %}e_{i}\equiv_{m_{j}}\delta_{ij}{% endequation %}, כאשר {% equation %}\delta_{ij}{% endequation %} הוא <strong>הדלתא של קרונקר</strong>:

{% equation %}\delta_{ij}=\begin{cases}1 & i=j\\0 & i\ne j\end{cases}{% endequation %}

כעת, נגדיר את הפתרון למערכת המשוואות: {% equation %}x=a_{1}e_{1}+a_{2}e_{2}+\dots+a_{k}e_{k}{% endequation %} (מודולו {% equation %}m{% endequation %}). כדי לראות שזה הפתרון המבוקש נשים לב לכך ש-{% equation %}x\equiv_{m_{i}}a_{1}\delta_{1i}+\dots+a_{k}\delta_{ik}=a_{i}{% endequation %}, כנדרש.

לאלו מכם שמכירים קצת אלגברה לינארית העסק הזה כנראה נראה מאוד מוכר - {% equation %}x{% endequation %} הוא צירוף לינארי של איזה משהו מוזר שנראה כמו בסיס אורתונורמלי, אבל הוא לא באמת בסיס כי אין פה מרחב וקטורי. זו בדיוק האנלוגיה שאני רוצה שתהיה לכם בראש; המתמטיקה עמוסה בסיטואציות כאלו שבהן יש לנו שני דברים שהם מאוד-דומים-אבל-לא-בדיוק-אותו-דבר.

זה מוכיח שהפתרון קיים. בשביל יחידות, נניח ש-{% equation %}x,y{% endequation %} הם שני פתרונות למערכת המשוואות. אז לכל {% equation %}i{% endequation %} מתקיים {% equation %}x-y\equiv_{m_{i}}a_{i}-a_{i}\equiv_{m_{i}}0{% endequation %}, כלומר {% equation %}m_{i}{% endequation %} מחלק את {% equation %}x-y{% endequation %} לכל {% equation %}i{% endequation %}. עכשיו, אם מספרים זרים מחלקים מספר כלשהו, גם המכפלה של כולם מחלקת את אותו מספר, ולכן נקבל ש-{% equation %}m{% endequation %} מחלק את {% equation %}x-y{% endequation %}, כלומר {% equation %}x\equiv_{m}y{% endequation %}, וסיימנו את הוכחת המשפט.

מה שחסר לי עדיין הוא הטענה הבאה, שעזרה לי למצוא את ה-{% equation %}d_{i}{% endequation %}-ים: אם {% equation %}a,n{% endequation %} הם מספרים זרים אז קיים {% equation %}x{% endequation %} כך ש-{% equation %}ax\equiv_{n}1{% endequation %}. הסיבה שהמתנתי עם הטענה הזו היא שזוהי טענה בסיסית עוד יותר בתורת המספרים שמשתמשים גם בה בכל מקום אפשרי בערך, ומדברים עליה בהקשרים רחבים הרבה יותר ממשפט השאריות הסיני. בבסיסה, הטענה הזו נובעת ממה שמכונה <strong>האלגוריתם האוקלידי</strong> שהקדשתי לו <a href="http://www.gadial.net/2011/09/12/euclidean_algorithm_and_rings/">פוסט כאן</a>. האלגוריתם הזה מאפשר, בהינתן שני מספרים שלמים {% equation %}a,b{% endequation %} שהמחלק המשותף הגדול ביותר שלהם הוא {% equation %}d{% endequation %}, למצוא שני מספרים שלמים {% equation %}x,y{% endequation %} כך ש-{% equation %}ax+by=d{% endequation %}; במקרה שלנו, שבו {% equation %}a,n{% endequation %} הם זרים, נקבל שיש {% equation %}x,y{% endequation %} כך ש-{% equation %}ax+ny=1{% endequation %}, וכשניקח את המשוואה הזו מודולו {% equation %}n{% endequation %} נקבל {% equation %}ax\equiv_{n}1{% endequation %}. במילים אחרות, מציאת ה-{% equation %}d_{i}{% endequation %}-ים המדוברת היא בסך הכל הפעלה של האלגוריתם האוקלידי (שהוא אלגוריתם <strong>מאוד</strong> מהיר).

שימו לב לעוד אבחנה מעניינת: ה-{% equation %}e_{i}{% endequation %}-ים שצצו בהוכחת המשפט <strong>אינם</strong> תלויים ב-{% equation %}a_{i}{% endequation %}-ים, אלא רק במודולוסים {% equation %}m_{i}{% endequation %}. זה אומר שאפשר לחשב אותם פעם אחת ולשמור בצד, ומרגע זה ואיך אפשר לפתור ביעילות כל מערכת משוואות מודולו {% equation %}m_{1},\dots,m_{k}{% endequation %} (לכל בחירה של {% equation %}a_{1},\dots,a_{k}{% endequation %}) בזמן קצר ביותר, בלי שיהיה צורך להפעיל שוב את האלגוריתם האוקלידי. (רק צריך לחשב את {% equation %}a_{1}e_{1}+a_{2}e_{2}+\dots+a_{k}e_{k}{% endequation %}, כלומר לבצע פעולה אחת של מכפלה סקלרית - וזה <strong>ממש ממש מהיר</strong>).

אם לחזור לחידה שבתחילת הפוסט, עכשיו ברור מה עשיתי שם - ראשית חשבתי על משחקי שבהם מספרי השחקנים הם מספרים זרים זה לזה (11 ו-5 באו מאליהם; כדי שיהיה מעניין הכנסתי גם את 9 לעניין). הבעיה הייתה שהחידה עם המודולוסים הללו הייתה בעלת הפתרון הלא מעניין "1" ולכן הכנסתי גם את 2 לתמונה. מכיוון שהמכפלה של כל המודולוסים יצאה 990, אמרתי שאין בשכבה יותר מ-1,000 תלמידים, כי היה מובטח לי שיש פתרון שקטן מ-990.

האם סיימנו? כן ולא. מה שהצגתי כרגע הוא הגרסה של המשפט כפי שהמתמטיקאים הסינים שהוכיחו אותו הכירו. אבל יש למשפט גם ניסוחים מודרניים יותר, שדורשים היכרות עם אלגברה קצת יותר מתקדמת ממה שדיברתי עליו בפוסט. המשך הפוסט יהיה מיועד, אם כן, למי שמכירים את המושגים הללו.

נתחיל מהחוג {% equation %}\mathbb{Z}_{n}{% endequation %} - השלמים מ-0 עד {% equation %}n-1{% endequation %} עם חיבור וכפל מודולו {% equation %}n{% endequation %}. זה בעצם המבנה האלגברי ש"עוטף" את החשבון המודולרי שדיברתי עליו קודם. את משפט השאריות הסיני אפשר לנסח מחדש בתור משפט על ה<strong>מבנה</strong> של {% equation %}\mathbb{Z}_{n}{% endequation %}. אם {% equation %}n=m_{1}\cdot m_{2}\cdots m_{k}{% endequation %} כאשר כל ה-{% equation %}m_{i}{% endequation %}-ים זרים זה לזה, אז משפט השאריות הסיני אומר ש-{% equation %}\mathbb{Z}_{n}\cong\mathbb{Z}_{m_{1}}\times\dots\times\mathbb{Z}_{m_{k}}{% endequation %}, כלומר {% equation %}\mathbb{Z}_{n}{% endequation %} איזומורפי למכפלה הקרטזית של ה-{% equation %}\mathbb{Z}_{m_{i}}{% endequation %}-ים. אם אתם לא מכירים את המושגים הללו, לצערי תתקשו להבין את הניסוח הזה, אבל אלו לא מושגים מורכבים עד כדי כך.

ההוכחה של המשפט היא קונסטרוקטיבית - אפשר להציג את האיזומורפיזם ישירות. באופן לא מפתיע, האיזומורפיזם הוא פשוט {% equation %}a\mapsto\left(a_{1},\dots,a_{k}\right){% endequation %} כאשר {% equation %}a_{i}=a\text{ mod }m_{i}{% endequation %}. לא קשה להראות שזה אכן הומומורפיזם; עיקר העבודה היא להראות שהוא חח"ע ועל, אבל זה בדיוק מה שמשפט השאריות הסיני נותן לנו: הוא אומר שלכל {% equation %}\left(a_{1},\dots,a_{k}\right){% endequation %} אפשר למצוא {% equation %}a{% endequation %} שמתמפה אליו (זה הפתרון למערכת המשוואות המודולרית שמוגדרת עבור {% equation %}\left(a_{1},\dots,a_{k}\right){% endequation %}), והוא אומר לנו שהפתרון הזה הוא יחיד, כלומר שאם שני איברים מתמפים לאותו {% equation %}\left(a_{1},\dots,a_{k}\right){% endequation %} הם חייבים להיות זהים. זה סוף הסיפור.

אבל אתם מכירים מתמטיקאים. אם הכללנו משהו וההכללה עובדת טוב, למה לא להכליל עוד? כרגע המשפט מנוסח רק על החוגים {% equation %}\mathbb{Z}_{n}{% endequation %}, אבל למה לא לקחת את זה צעד אחד קדימה?

עד כה זירת המשחק שלנו הייתה {% equation %}\mathbb{Z}{% endequation %}, המספרים השלמים. ההכללה הטבעית של {% equation %}\mathbb{Z}{% endequation %} היא חוג קומוטטיבי עם יחידה {% equation %}R{% endequation %}. כעת, מה היחס בין {% equation %}\mathbb{Z}_{n}{% endequation %} ובין {% equation %}\mathbb{Z}{% endequation %}? פשוט מאוד - {% equation %}\mathbb{Z}_{n}{% endequation %} הוא <strong>חוג מנה</strong> של {% equation %}\mathbb{Z}{% endequation %} שמתקבל על ידי חלוקה באידאל {% equation %}n\mathbb{Z}=\left\{ na\ |\ a\in\mathbb{Z}\right\} {% endequation %} (כלומר, {% equation %}\mathbb{Z}_{n}=\mathbb{Z}/n\mathbb{Z}{% endequation %}). אם כן, יהיו {% equation %}A_{1},\dots,A_{k}{% endequation %} אידאלים ב-{% equation %}R{% endequation %} (תתי-חוגים שבולעים ביחס לפעולת הכפל, כלומר {% equation %}ar\in A{% endequation %} לכל {% equation %}a\in A{% endequation %} ו-{% equation %}r\in R{% endequation %}), והאנלוגים של {% equation %}\mathbb{Z}_{m_{i}}{% endequation %} יהיו חוגי המנה {% equation %}R/A_{i}{% endequation %}.

אנו נזקקים לאנלוג לתכונת ה-"ה-{% equation %}m_{i}{% endequation %}-ים זרים בזוגות". אין משמעות לאמירה כמו "ה-{% equation %}A_{i}{% endequation %}-ים זרים בזוגות" כי "זר" דורש מושג של חלוקה שלא קיים באידאלים באופן כללי. לכן אולי כדאי לנסות ולהיזכר <strong>למה</strong> היה לנו צורך שה-{% equation %}m_{i}{% endequation %}-ים יהיו זרים בזוגות ולהכליל את התכונה הזו לחוגים. הצורך היה כדי שנוכל להשתמש בטענה המתמטית ההיא על כך שאם {% equation %}a,b{% endequation %} זרים אז קיימים {% equation %}x,y{% endequation %} כך ש-{% equation %}ax+by=1{% endequation %}. כשזה מנוסח בלשון ה-{% equation %}\mathbb{Z}_{n}{% endequation %}-ים, זו בעצם הטענה שאם {% equation %}a,b{% endequation %} זרים אז {% equation %}a\mathbb{Z}+b\mathbb{Z}=\mathbb{Z}{% endequation %}, כשחיבור אידאלים הוא במובן הטבעי המתבקש - איברי הסכום של האידאלים הם סכומים של איבר מהאידאל הראשון ואיבר מהאידאל השני.

את התכונה הזו נכליל: נאמר ששני אידאלים של {% equation %}R{% endequation %}, {% equation %}A,B{% endequation %} הם <strong>קו-מקסימליים</strong> אם {% equation %}A+B=R{% endequation %} (אני לא בטוח אם יש שם טוב יותר בעברית; באנגלית comaximal הוא שם מצויין שכן "זרים בזוגות" הוא coprime, וב-{% equation %}\mathbb{Z}{% endequation %} אידאל ראשוני הוא בפרט אידאל מקסימלי).

עכשיו, איך {% equation %}\mathbb{Z}_{n}{% endequation %} קשור ל-{% equation %}\mathbb{Z}_{m_{i}}{% endequation %}-ים במשפט המקורי? בכך ש-{% equation %}n{% endequation %} הוא המכפלה של כל ה-{% equation %}m_{i}{% endequation %}-ים. צריך למצוא אנלוג גם לזה, ולמרבה המזל אחד כזה מגיע באופן טבעי (שלא יפתיע אף אחד שמכיר את האופן שבו אידאלים מכלילים, רעיונית, מספרים שלמים; דיברתי על זה <a href="http://www.gadial.net/2011/08/21/algebraic_number_theory_intro_2/">בעבר בבלוג</a>). המושג המתאים הוא מכפלה של אידאלים, שמוגדרת באופן שהוא אולי קצת קשה לעיכול ממבט ראשון: המכפלה {% equation %}A_{1}A_{2}\cdots A_{k}{% endequation %} מוגדרת בתור קבוצת כל הסכומים הסופיים של מכפלות מהצורה {% equation %}a_{1}\cdots a_{k}{% endequation %} כאשר {% equation %}a_{i}\in A_{k}{% endequation %}. תרגיל טוב כדי לעכל את ההגדרה הזו היא להוכיח לעצמכם ש-{% equation %}m_{1}\mathbb{Z}\cdots m_{k}\mathbb{Z}=n\mathbb{Z}{% endequation %}.

כעת אפשר לנסח את משפט השאריות הסיני בניסוח האלגברי הכללי שלו:

אם {% equation %}R{% endequation %} הוא חוג קומוטטיבי עם יחידה ו-{% equation %}A_{1},\dots,A_{k}{% endequation %} הם אידאלים ב-{% equation %}R{% endequation %} שהם קו-מקסימליים בזוגות, אז {% equation %}R/A_{1}\cdots A_{k}\cong R/A_{1}\times\dots\times R/A_{k}{% endequation %}.

ההוכחה, שלא במפתיע, היא בעצם אותה הוכחה שכבר ראינו, פרט לכך שאפשר קצת לפשט אותה בגלל המסגרת הכללית של תורת החוגים, אבל גם צריך לעבוד טיפה כדי להוכיח דברים שעבור שלמים אני מניח כמעט כמובנים מאליהם. הדבר המרכזי שאני צריך לעשות הוא להוכיח שאם {% equation %}A_{1},\dots,A_{k}{% endequation %} הם קו-מקסימליים בזוגות, אז לכל {% equation %}i{% endequation %}, {% equation %}A_{i}{% endequation %} ו-{% equation %}\prod_{j\ne i}A_{j}{% endequation %} (כלומר, האדיאל שהוא מכפלת כל האידאלים {% equation %}A_{1},\dots,A_{k}{% endequation %} פרט ל-{% equation %}A_{i}{% endequation %}) הם קו-מקסימליים בזוגות. כדי להוכיח את זה מספיק להוכיח טענה פשוטה קצת יותר: אם {% equation %}A,B,C{% endequation %} הם אידאליים קו-מקסימליים בזוגות, אז {% equation %}A{% endequation %} ו-{% equation %}BC{% endequation %} קו-מקסימליים; אחרי שהוכחתי את זה אפשר להוכיח את הטענה הכללית באינדוקציה (בכל פעם {% equation %}B{% endequation %} יהיה מכפלה של כמה אידאלים ו-{% equation %}C{% endequation %} יהיה אידאל חדש שרוצים לצרף למכפלה).

מכיוון שאנחנו בחוג עם יחידה, די להראות שקיימים {% equation %}a\in A{% endequation %} ו-{% equation %}b\in B{% endequation %}, {% equation %}c\in C{% endequation %} כך ש-{% equation %}a+bc=1{% endequation %} כדי להוכיח ש-{% equation %}A{% endequation %} ו-{% equation %}BC{% endequation %} הם קו-מקסימליים. מתוך ההנחה שלנו, אנחנו יודעים שמתקיים {% equation %}a_{1}+b=1{% endequation %} ו-{% equation %}a_{2}+c=1{% endequation %} עבור {% equation %}a_{1},a_{2}\in A{% endequation %} ו-{% equation %}b\in B{% endequation %}, {% equation %}c\in C{% endequation %} כלשהם; נכפול אותם ונקבל {% equation %}a_{1}a_{2}+a_{1}c+a_{2}b+bc=1{% endequation %}, וסכום שלושת האיברים הראשונים הוא איבר ב-{% equation %}A{% endequation %} (במילים אחרות, {% equation %}a=a_{1}a_{2}+a_{1}c+a_{2}b{% endequation %}), כך שסיימנו.

כעת נעבור להוכחת משפט השאריות הסיני עצמו. מספיק להוכיח קיום של הומומורפיזם על {% equation %}R\to R/A_{1}\times\dots\times R/A_{k}{% endequation %} שהגרעין שלו הוא {% equation %}A_{1}\cdots A_{k}{% endequation %} והתוצאה תנבע ממשפט האיזומורפיזם הראשון לחוגים. ההומומורפיזם, שלא במפתיע, יהיה {% equation %}r\mapsto\left(r+A_{1},\cdots,r+A_{k}\right){% endequation %}. אם {% equation %}r{% endequation %} התמפה ל-{% equation %}0{% endequation %}, אז {% equation %}r\in A_{i}{% endequation %} לכל {% equation %}i{% endequation %}, כלומר {% equation %}r\in A_{1}\cap\cdots\cap A_{k}{% endequation %}, ומכאן קל לראות שהגרעין הוא {% equation %}A_{1}\cap\cdots\cap A_{k}{% endequation %} (ברור שכל איבר של {% equation %}A_{1}\cap\cdots\cap A_{k}{% endequation %} יתמפה לאפס).

כעת, {% equation %}A_{1}\cap\cdots\cap A_{k}=A_{1}\cdots A_{k}{% endequation %} במקרה הנוכחי, שבו כל זוג {% equation %}A_{i}{% endequation %}-ים הם קו-מקסימליים; זה האנלוג של העובדה עבור מספרים שלמים ש-{% equation %}\text{lcm}{% endequation %} (כפולה משותפת מינימלית) של מספרים שלמים שווה למכפלה שלהם אם כולם זרים. בכיוון אחד, כל איבר של {% equation %}A_{1}\cdots A_{k}{% endequation %} בוודאי שייך לכל אחד מהאידאלים, בשל תכונת הבליעה שלהם (מי שמורכב ממכפלה של איבר ב-{% equation %}A_{i}{% endequation %} ועוד דברים על בטוח יהיה ב-{% equation %}A_{i}{% endequation %}, וגם סכומים של איברים כאלו). בכיוון השני בואו ניקח איבר {% equation %}c\in A_{1}\cap\cdots\cap A_{k}{% endequation %} ונוכיח ש-{% equation %}c\in A_{1}\cdots A_{k}{% endequation %}.

כעת, {% equation %}A_{1}{% endequation %} ו-{% equation %}A_{2}A_{3}\cdots A_{k}{% endequation %} הם קו-מקסימליים, כך שקיימים {% equation %}a\in A_{1}{% endequation %} ו-{% equation %}b\in A_{2}A_{3}\cdots A_{k}{% endequation %} כך ש-{% equation %}1=a+b{% endequation %}. נכפול את שני האגפים ב-{% equation %}c{% endequation %} ונקבל {% equation %}c=ca+cb{% endequation %}. ברור לנו ש-{% equation %}cb\in A_{1}\cdots A_{k}{% endequation %} כי הוא מכפלה של איבר מ-{% equation %}A_{1}{% endequation %} ({% equation %}c{% endequation %}) עם איבר מ-{% equation %}A_{2}\cdots A_{k}{% endequation %} ({% equation %}b{% endequation %}), לכן נותר להוכיח ש-{% equation %}ca\in A_{1}\cdots A_{k}{% endequation %}, ולצורך כך מספיק להראות ש-{% equation %}c\in A_{2}\cdots A_{k}{% endequation %}, כלומר צמצמנו את הבעיה ממכפלה של {% equation %}k{% endequation %} איברים למכפלה של {% equation %}k-1{% endequation %} איברים וניתן להמשיך לעשות זאת עד אשר נגיע לאידאל בודד שעבורו הטענה טריוויאלית.

כל מה שנותר לעשות הוא להראות שההומומורפיזם שהגדרתי לעיל הוא באמת הומומורפיזם (אוותר על התענוג, זה לא קשה) ושהוא על. להוכיח שהוא על זה <strong>בדיוק</strong>, אבל בדיוק כמו במשפט ה"קלאסי": לכל {% equation %}A_{i}{% endequation %}, אנחנו יודעים שהוא קו-מקסימלי עם {% equation %}B=\prod_{j\ne i}A_{j}{% endequation %} (אני משתמש כאן ב-{% equation %}B{% endequation %} לצורכי נוחות בלבד). אז קיימים {% equation %}x_{i}\in A_{i},e_{i}\in B{% endequation %} כך ש-{% equation %}x_{i}+e_{i}=1{% endequation %}, או בלשון קוסטים, {% equation %}e_{i}+A_{i}=1+A_{i}{% endequation %}.

כעת, יהא וקטור {% equation %}\left(a_{1}+A_{1},\dots,a_{k}+A_{k}\right){% endequation %} של קוסטים. נגדיר {% equation %}r=a_{1}e_{1}+\dots+a_{k}e_{k}{% endequation %}. מהו {% equation %}r+A_{i}{% endequation %}? ובכן, לכל {% equation %}e_{j}{% endequation %} עבור {% equation %}j\ne i{% endequation %} אנחנו יודעים ש-{% equation %}e_{j}{% endequation %} שייך למכפלה של אידאלים שכוללים את {% equation %}A_{i}{% endequation %} ולכן {% equation %}e_{j}\in A_{i}{% endequation %} ולכן {% equation %}a_{j}e_{j}\in A_{i}{% endequation %} והגורם הזה נבלע בתוך {% equation %}A_{i}{% endequation %} (האנלוג עבור {% equation %}\mathbb{Z}_{m_{i}}{% endequation %} היה התאפסות), ואילו עבור {% equation %}e_{i}{% endequation %} אנחנו יודעים ש-{% equation %}e_{i}+A_{i}=1+A_{i}{% endequation %} ולכן {% equation %}a_{i}e_{i}+A_{i}=a_{i}+A_{i}{% endequation %} - בדיוק מה שרצינו. זה מסיים את ההוכחה.

מה שאני אוהב כל כך במשפט הזה, פרט לכך שהוא שימושי במגוון יישומים (נראה אחד בפוסט הבא), הוא העובדה שאפשר לראות אותו בשתי דרכים שונות - אחת מאוד קונקרטית ופרטית, ברמה שבה אפשר להבין מה קורה במשפט כמעט בלי להכיר מושגים קודם, והשניה ברמה יותר מופשטת שדורשת היכרות עם מושגים מתקדמים מעט יותר (לא <strong>הרבה</strong> יותר...), וכל אחת מנקודות המבט הללו מעשירה אותנו ומאפשרת לנו להבין יותר טוב "מה הולך פה", אבל אחרי שמתרגלים רואים ששתיהן הן בעצם אותו הדבר בדיוק. כמו שאני אוהב לצטט לפעמים: "המתמטיקה היא האמנות של קריאה באותו השם לדברים שונים, ושל קריאה בשמות שונים לאותו דבר".

