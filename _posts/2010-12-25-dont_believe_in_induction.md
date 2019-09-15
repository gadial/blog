---
id: 897
title: "גם אני לא מאמין באינדוקציה (כי לאמונה אין קשר לזה)"
date: 2010-12-25 00:27:29
layout: post
categories: 
  - הגיגים מתמטיים כלליים
tags: 
  - אינדוקציה מתמטית
  - הוכחות
  - מתמטיקה תיכונית
---
אינדוקציה מתמטית היא אחד מהכלים הבסיסיים שברשותו של המתמטיקאי. בניגוד לרושם שעשוי להתקבל בתיכון כאילו היא מתאימה לטיפול רק במחלקה משמימה כלשהי של אי שוויונים, אינדוקציה צצה ועולה בכל מקום במתמטיקה בערך. לכן נראה לי שכדאי להקדיש פוסט בנסיון להסביר מהי בכלל אינדוקציה ולמה היא אינה רמאות.

רגע, מי אומר שהיא רמאות? ובכן, לא מעט אנשים, לצערי. נראה לי שלכל סטודנט למתמטיקה יצא להיתקל פעם במישהו ש"לא מאמין באינדוקציה" (או לפחות לא מבין למה זה עובד). ברוח הזמנים, המקום הטוב ביותר להביא בו אסמכתא הוא פייסבוק: מישהו טרח להקים <a href="http://www.facebook.com/group.php?gid=28119106039">קבוצת פייסבוק</a> שססמתא היא "גם אני לא מאמין באינדוקציה". אני משער שהוא לפחות חצי הומוריסטי, אך התיאור של הקבוצה לא שונה מהותית מטענות ששמעתי גם בהזדמנויות אחרות ונאמרו לפעמים ברצינות תהומית:
<blockquote>נכון מוכיחים לכם דברים באינדוקציה לכל אורך התואר, וזה נראה כמו בולשיט טהור? בתכלס, מה זה אינדוקציה ? זה לקחת להגיד: הנה מה שאני רוצה להוכיח בואו נניח שזה נכון וכפי שראינו קודם, זה נכון מ.ש.ל

ולכן, אנחנו מתנגדים בתוקף לאינדוקציה, ודורשים שתבוטל תוקף ההוכחה שלה לאלתר. וכך לא ידרשו מאתנו להוכיח יותר דברים באינדוקציה</blockquote>
ובכן, כן - למה אינדוקציה היא <strong>לא</strong> מה שמתואר כאן? מה זו בכלל אינדוקציה?

באופן כללי, לא רק במתמטיקה, "אינדוקציה" בא לתאר הסקה מהפרט אל הכלל. נוהגים להבדיל את האינדוקציה המדעית הרגילה, שבה מנסים להסיק מסקנה כללית ממדגם רחב של מקרים פרטיים, מהאינדוקציה המתמטית שמנסה להיות יותר מדויקת ואמינה, כך שאסתפק בלדבר כאן רק על מה שנקרא "אינדוקציה מתמטית". גם באינדוקציה מתמטית מנסים לעשות הליך של הסקה מהפרט אל הכלל. הרעיון הוא שאם מנסים להוכיח טענה כלשהי על קבוצה רחבה של אובייקטים, אפשר לעשות זאת "צעד צעד"; במקום להוכיח את הטענה על כל האובייקטים בבת אחת (מה שעשוי להיות קשה מאוד), אפשר ראשית להוכיח אותה על קבוצה קטנה של אובייקטים פשוטים יחסית. אחר כך אפשר להתרחב טיפה ולהוכיח את הטענה על קבוצה קצת יותר גדולה של אובייקטים, <strong>תוך שאנו נעזרים</strong> בידע שכבר יש לנו - שהטענה נכונה לקבוצה הקטנה של האובייקטים הפשוטים. אט אט אנחנו מרחיבים את ההוכחה שלנו כך שתכלול עוד ועוד מקרים, ובכל שלב של ההרחבה אנו נעזרים במה שכבר הוכחנו עד כה.

מה שתיארתי עד כה לא נראה שונה כל כך ממה שמתמטיקאים עושים באופן כללי - בדרך להוכחת טענה קשה כלשהי הם מוכיחים משפטי עזר, לרוב באופן שבו הוכחה של משפט אחד מסתמכת על נכונות המשפטים שקדמו לו. מה שמבדיל אינדוקציה מהמקרים הללו הוא הפשטות שלה; כדי להשתמש באינדוקציה מספיק להוכיח שני דברים: ראשית, שהטענה נכונה עבור "קבוצת בסיס" של אובייקטים פשוטים; ושנית, ש"אם הטענה נכונה עבור קבוצת אובייקטים כלשהי, אז אפשר להוכיח אותה גם לקבוצת אובייקטים רחבה יותר". תחת תנאים מסויימים על האובייקטים שההוכחה עוסקת בהם, זה כל מה שצריך כדי להוכיח את הטענה לכל האובייקטים.

עד כה דיברתי מאוד באוויר ולכן בואו נעבור לדוגמאות שעוסקות בקבוצת האובייקטים ה"קלאסית" שעליה מדברים כשמדברים על אינדוקציה מתמטית - המספרים הטבעיים, {% equation %}1,2,3,\dots{% endequation %}. בניסוח עבור מספרים טבעיים, אינדוקציה מתמטית אומרת את הדבר הבא: "אם תכונה כלשהי מתקיימת עבור המספר 1, ואם קיום התכונה עבור המספר {% equation %}n{% endequation %} גורר את הקיום שלה עבור המספר {% equation %}n+1{% endequation %}, אז התכונה נכונה לכל המספרים הטבעיים". הניסוח הזה כה חשוב עד כי במערכת האקסיומות הסטנדרטית למספרים הטבעיים הוא נכלל כאחת מהאקסיומות ("אקסיומת האינדוקציה"). אין זה אומר שאנו מניחים שאינדוקציה היא משהו שנכונותו אינה דורשת הצדקה; אחרי שאציג דוגמה פשוטה נעבור לדיון בשאלה למה בכלל נכון להניח שאינדוקציה מתמטית "עובדת".

דוגמה קלאסית להוכחה באינדוקציה היא ההוכחה לנוסחת הסכום של כל המספרים הטבעיים מ-1 ועד {% equation %}n{% endequation %}: {% equation %}1+2+3+\dots+n=\frac{n\left(n+1\right)}{2}{% endequation %}. אי אפשר להביא את הנוסחה הזו מבלי לספר את הסיפור שנלווה אליה למרות שאין לו שום קשר לאינדוקציה מתמטית: מספרים שהמורה של גאוס הקטן (שהיה בן 6? 7? משהו בסגנון...) התעצל יום אחד וכדי שיהיה לו שקט מהתלמידים נתן להם לסכם את כל המספרים מ-1 ועד 100 (כלומר, במקרה הזה {% equation %}n=100{% endequation %}). התלמידים מן הסתם לא הכירו את הנוסחה. והנה אחרי דקה או שתיים בא גאוס אל המורה ונתן לו את הפתרון - 5050. למורה ההמום הוא הסביר את ההגיון שלו - אם סוכמים את האיבר הראשון והאחרון, שהם {% equation %}1{% endequation %} ו-{% equation %}n{% endequation %}, מקבלים {% equation %}n+1{% endequation %}; ואם סוכמים את האיבר השני והלפני אחרון, שהם {% equation %}2{% endequation %} ו-{% equation %}n-1{% endequation %}, מקבלים גם {% equation %}n+1{% endequation %}, וכן הלאה. כמה זוגות כאלו יש בסך הכל? בדיוק חצי ממספר האיברים, כלומר {% equation %}\frac{n}{2}{% endequation %}. לכן סכום כל האיברים הוא {% equation %}\frac{n}{2}\left(n+1\right){% endequation %}. אני לא יודע אם גאוס אכן גילה כך את הנוסחה או שזה סתם צ'יזבט, אבל לטעמי זו הוכחה נפלאה ממש.

חזרה לאינדוקציה מתמטית. ההוכחה באינדוקציה של נכונות הנוסחה היא הרבה יותר משעממת לצערי, אבל זכרו שמדובר על דוגמה שמנסה להיות פשוטה ואולי גם תפיס את דעתם של אלו שלא נחה עליהם דעתם מההוכחה של גאוס במקרה שבו {% equation %}n{% endequation %} הוא אי זוגי - למרות שאפשר לנסח אותה בצורה שתטפל גם בה. צריך להתחיל מהוכחה שהטענה נכונה עבור {% equation %}n=1{% endequation %}, אבל זה פשוט עניין של הצבה בנוסחה ובדיקה: אם מציבים {% equation %}n=1{% endequation %} מקבלים {% equation %}\frac{1\cdot\left(1+1\right)}{2}=1{% endequation %}. השיעמום הזה עשוי ליצור את הרושם שהוכחת הבסיס היא תמיד טריוויאלית, ולא כן - לפעמים הוכחת הבסיס היא החלק המאתגר יותר בהוכחה באינדוקציה.

הצעד הוא כזה: אנו מניחים שכבר ידוע לנו כי {% equation %}1+2+\dots+n=\frac{n\left(n+1\right)}{2}{% endequation %}. כעת אנו רוצים להוכיח את השלב הבא, כלומר שמתקיים {% equation %}1+2+\dots+n+\left(n+1\right)=\frac{\left(n+1\right)\left(n+2\right)}{2}{% endequation %}. מה עושים? משתמשים במה שכבר הוכחנו. אנחנו יודעים את סכום {% equation %}n{% endequation %} האיברים הראשונים, ולכן אגף שמאל של המשוואה הוא פשוט {% equation %}\frac{n\left(n+1\right)}{2}+\left(n+1\right){% endequation %} וכעת כל מה שנותר הוא לעשות חשבון פשוט:

{% equation %}\frac{n\left(n+1\right)}{2}+\left(n+1\right)=\frac{n\left(n+1\right)+2\left(n+1\right)}{2}=\frac{\left(n+1\right)\left(n+2\right)}{2}{% endequation %}

למי שהמעבר האחרון לא ברור לו - הוצאתי את הגורם המשותף {% equation %}\left(n+1\right){% endequation %} משני המחוברים.

אם כן, זה כל מה שהיה צריך להוכיח, ועכשיו הנוסחה נכונה באופן כללי. אבל למה מה שעשיתי הוא לא לומר "הנה מה שאני רוצה להוכיח בואו נניח שזה נכון וכפי שראינו קודם, זה נכון מ.ש.ל"? בפשטות, כי אני לא מניח שמה שאני רוצה להוכיח הוא נכון, אלא ש<strong>מה שכבר הוכחתי</strong> הוא נכון, ואני נעזר במה שכבר הוכחתי כדי לבנות הוכחה חדשה. הוכחה של הטענה עבור {% equation %}n=4{% endequation %}, למשל, תלך כך: "ראשית, ראינו שהטענה נכונה עבור 1. שנית, ראינו שאם הטענה נכונה עבור 1 אז היא נכונה גם עבור 2, ולכן היא נכונה עבור 2. שלישית, ראינו שאם הטענה נכונה עבור 2 אז היא נכונה גם עבור 3, ולכן היא נכונה עבור 3; ולסיום, ראינו שאם היא נכונה עבור 3 אז היא נכונה גם עבור 4, ולכן היא נכונה גם עבור 4 - סיימנו". כלומר, ההוכחה של הטענה עבור 4 מתבססת על כך שקודם כל אנחנו כותבים במפורש את ההוכחה עבור 1, ואז את ההוכחה עבור 2, ואז את ההוכחה עבור 3 ולסיום את ההוכחה עבור 4, כשכל צעד בהוכחה מתבסס על הצעדים שקדמו לו.

במקרה הפרטי של הטענה שלנו זה הולך כך. ראינו שסכום כל האיברים עד 1 הוא 1; לכן סכום כל האיברים עד 2 הוא סכום כל האיברים עד 1 (שהוא 1) ועוד 2, כלומר 3; ולכן סכום כל האיברים עד 3 הוא סכום של האיברים עד 2 (שראינו לפני שניה שהוא 3) ועוד 3, כלומר 6; ולכן סכום כל האיברים עד 4 הוא סכום כל האיברים עד 3 (שראינו לפני רגע שהוא 6) ועוד 4, כלומר 10, ו-10 הוא בדיוק {% equation %}\frac{4\left(4+1\right)}{2}{% endequation %}, כמו שרצינו. לכן הטענה נכונה גם עבור 4.

בעצם, השלב שאנו קוראים לו "צעד האינדוקציה" הוא <strong>תבנית הוכחה</strong>. הוא הוכחה שתלויה בפרמטר {% equation %}n{% endequation %}, שאפשר להציב בו כל מספר טבעי. אם אציב בתבנית שלמעלה את המספר 3 אני אקבל הוכחה חוקית לגמרי לטענה "אם {% equation %}1+2+3=\frac{3\left(3+1\right)}{2}{% endequation %} אז {% equation %}1+2+3+4=\frac{4\left(4+1\right)}{2}{% endequation %}", וכך יקרה לכל מספר אחר שאציב ב-{% equation %}n{% endequation %}. העניין הוא בכך ש<strong>מתמטיקאים הם עצלנים</strong>. הם לא רוצים לחזור שוב ושוב על אותה הוכחה. הם רואים שאין שום הבדל מהותי בין ההוכחה של "אם הטענה נכונה עבור 2 אז היא נכונה עבור 3" ובין ההוכחה של "אם הטענה נכונה עבור 3 אז היא נכונה עבור 4" ולכן הם מסתפקים בתבנית אחת שמטפלת <strong>בכל המקרים האפשריים בבת אחת</strong>. אולי זה לא ברור מייד אך קורה כאן קסם מסויים - איכשהו, למרות שלא כתבנו הוכחה פורמלית לאף אחד מהמספרים פרט ל-1 (אלא רק סיפקנו את התבנית), פתאום קיבלנו הוכחה עבור כל <strong>אינסוף</strong> המספרים הטבעיים. למי שלא משתכנע עדיין, חשבו על זה כך: אם הטענה אינה נכונה עבור כל אינסוף הטבעיים, אז קיים מספר טבעי כלשהו - נקרא לו {% equation %}m{% endequation %} - שעבורו הטענה לא נכונה. כעת, הטענה נכונה עבור 1 (מהבסיס), ואם היא נכונה עבור 1 אז היא נכונה גם עבור 2 (מהצעד) ולכן גם עבור 3 (מהצעד) וכן הלאה וכן הלאה... בסוף נגיע ל-{% equation %}m{% endequation %} ונקבל שהטענה נכונה גם עבור {% equation %}m{% endequation %}. מכיוון שלא הנחנו כלום על {% equation %}m{% endequation %}, המסקנה היא שלא קיים {% equation %}m{% endequation %} טבעי שעבורו הטענה אינה מתקיימת, ולכן היא אכן מתקיימת עבור אינסוף הטבעיים. הפאנץ' פה (וארחיב על כך בהמשך) הוא שלכל מספר טבעי יש רק מספר <strong>סופי</strong> של מספרים שבאים לפניו ולכן אפשר לבנות "שרשרת" הוכחה שמגיעה מהבסיס אל {% equation %}m{% endequation %}, לכל {% equation %}m{% endequation %}.

דרך יפה להמחיש את מה שקורה באינדוקציה הוא לתאר אותה בעזרת אבני דומינו: אם אנחנו מפילים את האבן הראשונה בשורה (<strong>בסיס האינדוקציה</strong>) והשורה בנויה כך שאם אבן נופלת, גם האבן הבאה אחריה נופלת (<strong>צעד האינדוקציה</strong>) אז כל האבנים בשורה יפלו.

אם כן, לסיום ההתנגדות לאינדוקציה אחזור על העניין העיקרי - באינדוקציה אנחנו אף פעם לא מניחים את המבוקש, אלא מניחים טענה קצת יותר חלשה מהמבוקש, שבאמצעותה אפשר להוכיח את המבוקש. השרשרת של ההסתמכויות הללו על "קצת יותר חלש" מסתיימת בבסיס האינדוקציה.

בואו נעבור לדבר הרבה יותר מטריד - האם אינדוקציה היא לא כלי חלש <strong>מדי</strong>? הרי כל מה שאני יכול לעשות הוא להוכיח איתה טענות על מספרים טבעיים! ובכן, לשאלה הזו יש שתי תשובות: לא, ולא. ה"לא" הראשון הוא שגם טענות על טבעיים יכולות בעצם להחביא בתוכן טענות על דברים שונים לחלוטין. הבה וניזכר בטענה ש<a href="http://www.gadial.net/?p=882">הוכחתי בפוסט הקודם</a> - הוכחתי שם שכל לוח משבצות בגודל {% equation %}2^{n}\times2^{n}{% endequation %} שהוסרה ממנו בדיוק משבצת אחת ניתן לריצוף בידי צורות "ר". כלומר, טענתי טענה על לוחות של משבצות, לא על מספרים טבעיים; ועם זאת, ההוכחה הייתה באינדוקציה. הכיצד? כי הטענה שלי, אם מנסחים אותה פורמלית עד הסוף, הייתה "לכל מספר טבעי {% equation %}n{% endequation %} מתקיימת התכונה שלוח שגודלו {% equation %}2^{n}\times2^{n}{% endequation %} והוסרה ממנו משבצת אחת ניתן לריצוף".

למעשה, מה שקרה כאן הוא שהוכחתי טענה על האובייקט "לוח" תוך ניצול העובדה שהמבנה של הלוחות שעניינו אותי הוא פשוט יחסית וניתן לתיאור באמצעות פרמטר שהוא מספר טבעי, ושאני יכול להוכיח את הטענה על לוח שמאופיין על ידי הפרמטר {% equation %}n+1{% endequation %} באמצעות הסתמכות על נכונות הטענה עבור לוחות שמאופיינים על ידי הפרמטר {% equation %}n{% endequation %}. פעמים רבות במתמטיקה השלב הראשון בדרך להוכחה באינדוקציה הוא בדיוק זיהוי המבנה של האובייקטים שעליהם רוצים להוכיח דבר מה כדי שיהיה ברור מי מהם מתאים למספר 1, מי מתאים ל-2 וכן הלאה.

אך למעשה, זה לא נגמר כאן. אין שום הכרח להסתפק באינדוקציות על מספרים טבעיים בלבד. הרחבה מיידית אחת של האינדוקציה היא לכל קבוצה סדורה היטב. קבוצה סדורה היטב היא קבוצה שאפשר להשוות בין כל שניים מאיבריה ולהגיד מי מהם קטן יותר, ובנוסף לכך מקיימת עוד תכונה (תכונת <strong>הסדר הטוב</strong>) והיא שלכל תת-קבוצה של איברים מתוכה יש איבר מינימלי. דוגמה לקבוצה שאינה סדורה היטב היא השלמים, {% equation %}\mathbb{Z}{% endequation %} - לה עצמה אין איבר מינימלי (למה?). לעומת זאת קבוצת הטבעיים {% equation %}\mathbb{N}{% endequation %} היא הדוגמה הקלאסית ביותר לקבוצה סדורה היטב.

ניסוח כללי של עקרון האינדוקציה לקבוצות סדורות היטב הוא זה: אם {% equation %}A{% endequation %} היא קבוצה סדורה היטב, ויש לנו תכונה כלשהי, אז כדי להוכיח שהתכונה מתקיימת לכל אברי {% equation %}A{% endequation %} מספיק להוכיח את הטענה הבאה, שאכנה "צעד האינדוקציה":

"לכל {% equation %}x\in A{% endequation %}, אם טענה כלשהי מתקיימת לכל {% equation %}y&lt;x{% endequation %} שנמצא ב-{% equation %}A{% endequation %} אז היא מתקיימת עבור {% equation %}x{% endequation %}".

שימו לב שכאן בכלל לא דיברתי על בסיס האינדוקציה אבל זה לא אומר שהוא לא שם - אם אני מוכיח את צעד האינדוקציה אני חייב תוך כדי כך גם להוכיח את בסיס האינדוקציה. מדוע? ובכן, עבור {% equation %}x\in A{% endequation %} שהוא האיבר המינימלי של {% equation %}A{% endequation %} כולה ({% equation %}A{% endequation %} היא סדורה היטב אז הוא קיים) פשוט לא קיימים איברים {% equation %}y&lt;x{% endequation %}, ולכן האמירה "הטענה מתקיימת לכל {% equation %}y&lt;x{% endequation %}" היא בודאות נכונה בלי קשר לכלום (מה שנקרא במתמטיקה "באופן ריק") ולכן כדי להוכיח את צעד האינדוקציה אני חייב להוכיח שהטענה מתקיימת עבור {% equation %}x{% endequation %} המינימלי מבלי שיהיה לי שום דבר להסתמך עליו.

זו דוגמה נחמדה לאופן שבו ברגע שבו מבצעים אבסטרקציה כלשהי לנושא הדיון שלנו ועוברים לדבר על מקרה כללי הרבה יותר, הניסוחים דווקא הופכים לפשוטים ואלגנטיים יותר (בהינתן, כמובן, שבכלל מצליחים להבין מה הולך כאן - וזה לא קל לעיכול בהתחלה). גם ההוכחה שהעקרון הזה "עובד" היא פשוטה: נניח שהוכחתי את צעד האינדוקציה, ועדיין יש איברים ב-{% equation %}A{% endequation %} שאינם מקיימים את התכונה. הבה ונתבונן בתת-הקבוצה של {% equation %}A{% endequation %} שכוללת בדיוק את כל האיברים שאינם מקיימים את התכונה. <strong>מכיוון ש-{% equation %}A{% endequation %} היא קבוצה סדורה היטב</strong>, קיים איבר מינימלי {% equation %}x{% endequation %} לאותה תת קבוצה. מכיוון שהוא האיבר המינימלי מבין כל האיברים שאינם מקיימים את התכונה, הרי שלכל {% equation %}y\in A{% endequation %} שמקיים {% equation %}y&lt;x{% endequation %} כן מתקיימת התכונה - אבל אז, מצעד האינדוקציה, נובע שהיא מתקיימת גם עבור {% equation %}x{% endequation %} - סתירה.

זה מוביל אותנו למושג האינדוקציה הטרנספיניטית. מושג שראוי לפוסט בפני עצמו וגם <a href="http://www.muchado.gadial.net/?p=7">זכה לכזה</a>, אבל עדיין לא אצלי. הרעיון באינדוקציה שכזו הוא להרחיב את הדיון מקבוצת כל המספרים הטבעיים לקבוצת כל הסודרים. אפילו להסביר מהו סודר זה יותר מדי לפוסט הנוכחי; רק אעיר שזהו עוד אחד מרעיונותיו המבריקים של קנטור, ממציא תורת הקבוצות, ומהווה הכללה מאוד יפה לרעיון של שימוש במספרים טבעיים לתיאור <strong>מספר סידורי</strong> של איברים (להבדיל משימוש במספרים טבעיים לתיאור "כמות" - זה ההבדל בין להגיד "אתה השביעי בתור" ולהגיד "יש בתור שבעה אנשים" - המספר 7 מופיע כאן בשני הקשרים שונים ולא זהים לגמרי), שמאפשר לשמור על מושג הסדר הזה גם כשמגיעים לגדלים אינסופיים. עקרון האינדוקציה שתיארתי לעיל משתלב יפה עם אוסף כל הסודרים, כך שניתן באמצעות אינדוקציה להוכיח שתכונה כלשהי מתקיימת לכל הסודרים הקיימים. כאמור, אני לא עושה הרבה יותר מלנפנף ידיים ולזרוק שמות מפוצצים כאן; המטרה שלי היא להמחיש עד כמה הרעיון הפשוט של אינדוקציה הוא חזק ומופיע בהקשרים רחבים בהרבה משנדמה במבט ראשון.

אפשר להכליל את מושג האינדוקציה גם באופן נוסף לפעמים יש לנו אובייקטים שנוצרים <strong>באופן אינדוקטיבי</strong>: מתחילים מקבוצה פשוטה של איברי בסיס, ואז בכל שלב בונים איבר חדש מתוך חלק מהאיברים הקיימים. דוגמה קלאסית לכך היא נוסחאות מתמטיות פורמליות; אובייקט הבסיס הוא מספר טבעי כלשהו, ואילו אם {% equation %}\alpha,\beta{% endequation %} הן שתי נוסחאות אז גם {% equation %}\left(\alpha+\beta\right){% endequation %} ו-{% equation %}\left(\alpha\times\beta\right){% endequation %} הן נוסחאות, למשל. בעזרת כללי הבניה הללו אנו רואים ש-{% equation %}\left(5+3\right)\times7{% endequation %} היא נוסחה בעוד ש-{% equation %}\left(5+3\right)\times2+9{% endequation %} דווקא אינה נוסחה "חוקית" (איפה הסוגריים סביב 9?). אם יש לנו קבוצת אובייקטים שכזו, אז כדי להוכיח עליה טענה מספיק להוכיח שהטענה מתקיימת עבור איברי הבסיס, ושאם מפעילים כלל בניה על אובייקטים שמקיימים את הטענה, אז גם התוצר מקיים את הטענה. שימו לב שזה זהה לאינדוקציה "רגילה" במספרים טבעיים עם "כלל הבניה" שלוקח מספר {% equation %}a{% endequation %} ומייצר ממנו את המספר {% equation %}a+1{% endequation %}. בלוגיקה מתמטית ובתחומים קרובים במדעי המחשב הוכחות כאלו הן נפוצות להחריד, עד שבדיחה ידועה אומרת שההבדל בין מדען מחשב ומתמטיקאי הוא שהמתמטיקאי יודע גם להוכיח דברים שלא באינדוקציה.

לסיום אני רוצה לומר משהו על הזהירות שצריך לנקוט בה כשמוכיחים משהו באינדוקציה. הנה הוכחה לכך שכל הסוסים בעולם שחורים: נוכיח באינדוקציה שבכל קבוצה בת {% equation %}n{% endequation %} סוסים, כל הסוסים באותו צבע (ומכיוון שאנו יודעים שקיים סוס שחור - "הסייח השחור" - אז כולם חייבים להיות בצבע שלו). הנה ההוכחה, באינדוקציה: עבור קבוצה בגודל {% equation %}n=1{% endequation %} ברור שכל הסוסים הם באותו צבע (כי יש בדיוק סוס אחד בקבוצה). נניח נכונות עבור {% equation %}n{% endequation %} ונוכיח עבור {% equation %}n+1{% endequation %}: בהינתן קבוצה בת {% equation %}n+1{% endequation %} סוסים ראשית נוציא ממנה סוס ונשמור אותו בצד, ונקבל מהנחת האינדוקציה שכל שאר הסוסים בקבוצה הם באותו צבע. כעת נחזיר את הסוס שהוצאנו, נוציא אחד אחר, ושוב נקבל שכל הסוסים בקבוצה הם באותו צבע, ולכן גם הסוס שקודם השארנו בצד הוא באותו צבע כמו כולם. מ.ש.ל.?

עצרו רגע וחשבו איפה רימיתי. כי הרי ברור שרימיתי - זה לא שכל מושג האינדוקציה קרס כרגע. למעשה, רימיתי באופן גרוע למדי - כמו עם <a href="http://www.gadial.net/?p=141">הפרדוקסים של זנון</a>, כך גם כאן, ככל שהלימודים המתמטיים שלי התקדמו גיליתי שיותר ויותר קשה לי לנסח את הרמאות הזו באופן משכנע.

ובכן, היכן הרמאות? הבסיס דווקא תקין לחלוטין (אף שהאינטואיציה אומרת שהוא בעייתי). הרמאות היא בצעד האינדוקציה, והיא עדינה יחסית - היא מתבססת על כך שאינטואיטיבית, אנחנו חושבים שבצעד האינדוקציה אנחנו מוכיחים את הטענה עבור {% equation %}n{% endequation %} "גדול", למרות שזה ממש לא זה. אנחנו מוכיחים את הטענה עבור {% equation %}n{% endequation %} <strong>כללי</strong>, וזה שונה מהותית. זה אומר שלהוכחה שלנו <strong>אסור</strong> להסתמך על הנחה סמויה כלשהי על הגודל של {% equation %}n{% endequation %}, למרות שזה בדיוק מה שאנחנו עושים כרגע. למה? כי את תעלול ריקון הקבוצה שלנו אפשר להפעיל באופן מוצלח רק אם {% equation %}n{% endequation %} הוא לפחות 3. אם {% equation %}n=2{% endequation %} אז יש בקבוצה רק שני סוסים - נקרא להם אליס ובוב. אם נוציא את אליס מהקבוצה יישאר בה רק בוב, וברור שבקבוצה שמכילה רק את בוב, לכל הסוסים יש את הצבע של בוב. ואז נכניס את אליס לקבוצה ונוציא ממנה את בוב, ושוב, לכל הסוסים בקבוצה יש את אותו צבע - הצבע של אליס - אבל זה לא אומר כלום על הצבע של בוב... ההנחה הסמויה היא שבקבוצת הסוסים שלנו יש גם "סוס מתווך" כלשהו שתמיד נשאר בקבוצה, ולכן הצבע שלו זהה גם לצבע של אליס וגם לצבע של בוב ולכן הצבעים של אליס ובוב זהים, אבל בקבוצה בגודל 2 לא קיים סוס מתווך כזה ולכן צעד האינדוקציה כושל פה.

לסיום, הערה אחת לקבוצת מתנגדי האינדוקציה בפייסבוק - לשניים וחצי מהם שמתכוונים לזה ברצינות, כלומר - אני בהחלט מזמין אתכם "לבטל" את האינדוקציה - בפעם הבאה שנותנים לכם תרגיל ואומרים לכם להוכיח באינדוקציה, אתם מוזמנים לעשות זאת בדרך אחרת (למיטב זכרוני אפילו בתיכון כבר נהוג להצמיד את "הוכיחו באינדוקציה או בכל דרך אחרת" לתרגילים - כמובן שזה בא לומר "מאוד, מאוד כדאי לכם להשתמש כאן באינדוקציה"). אם לא תצליחו - ובכן, לא נורא, העיקר שאתם אנשי עקרונות.