---
title: "תורת הקבוצות - קבוצות סדורות היטב"
layout: post
categories:
  - תורת הקבוצות
tags:
  - קבוצות סדורות היטב
image: "/assets/img/main/set_theory.png"
---


<h2>מבוא</h2>

בסדרת הפוסטים שלי על תורת הקבוצות <a href="https://gadial.net/2020/01/10/order_relations/">הצגתי מתישהו</a> את המושג של <strong>יחס סדר</strong>. בפוסט הזה אני רוצה לדבר על סוג חשוב ומועיל של יחסי סדר: <strong>סדר טוב</strong>. בואו נתחיל קודם כל מההגדרות.

כזכור, יחס סדר {% equation %}\le{% endequation %} מעל קבוצה {% equation %}A{% endequation %} הוא יחס (קבוצה של זוגות של אברי {% equation %}A{% endequation %}, כלומר תת-קבוצה של {% equation %}A\times A{% endequation %}) שהוא

<ul> <li><strong>רפלקסיבי</strong>: לכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a\le a{% endequation %}.</li>


<li><strong>טרנזיטיבי</strong>: אם {% equation %}a\le b{% endequation %} וגם {% equation %}b\le c{% endequation %} אז {% equation %}a\le c{% endequation %}</li>


<li><strong>אנטיסימטרי</strong>: אם {% equation %}a\le b{% endequation %} וגם {% equation %}b\le a{% endequation %} אז {% equation %}a=b{% endequation %}.</li>

</ul>

לפעמים מגדירים יחס סדר גם בצורה שונה, ובה מסמנים אותו {% equation %}<{% endequation %}; הוא עדיין צריך להיות טרנזיטיבי, אבל עכשיו הוא צריך להיות גם א-רפלקסיבי, כלומר {% equation %}a\not<a{% endequation %} לכל {% equation %}a\in A{% endequation %}. זה ניסוח קצת יותר "חסכוני" כי אנטיסימטריה לא יכולה להתקיים: אם {% equation %}a<b{% endequation %} וגם {% equation %}b<a{% endequation %} נובע מטרנזיטיביות {% equation %}a<a{% endequation %}, מה שאמרנו שלא קורה. שני הניסוחים שמישים ומקובלים וקל לעבור מאחד לשני: אם {% equation %}\le{% endequation %} הוא יחס סדר על פי הניסוח הראשון, נגדיר ש-{% equation %}a<b{% endequation %} אם ורק אם {% equation %}a\le b{% endequation %} וגם {% equation %}a\ne b{% endequation %} וקיבלנו את יחס הסדר השני {% equation %}<{% endequation %}, ובאופן דומה אם אנחנו מתחילים מ-{% equation %}<{% endequation %} אז נגדיר {% equation %}a\le b{% endequation %} אם ורק אם {% equation %}a<b{% endequation %} או {% equation %}a=b{% endequation %} וקיבלנו את {% equation %}\le{% endequation %}. בגלל ששני סוגי היחסים קשורים עד כדי כך לפעמים ארשה לעצמי להשתמש באחד ולפעמים בשני, לפי מה שיוצא ומתאים.

יחס סדר הוא <strong>מלא</strong> (או <strong>לינארי</strong>) אם אפשר להשוות כל שני איברים, כלומר לכל {% equation %}a,b\in A{% endequation %} או ש-{% equation %}a\le b{% endequation %} או ש-{% equation %}b\le a{% endequation %}. ואיבר {% equation %}a\in A{% endequation %} הוא <strong>איבר ראשון</strong> על פי יחס הסדר, אם לכל {% equation %}b\in A{% endequation %} מתקיים {% equation %}a\le b{% endequation %}. 

עכשיו אפשר להגדיר מה זה סדר טוב: זה יחס סדר <strong>מלא</strong> שבו לכל תת-קבוצה לא ריקה של {% equation %}A{% endequation %} קיים <strong>איבר ראשון</strong>. לזוג {% equation %}\left(A,\le\right){% endequation %} של הקבוצה ויחס הסדר הטוב עליה קוראים <strong>קבוצה סדורה היטב</strong>.

בואו נראה דוגמאות. והרבה. כי מה הטעם בהגדרה בלי דוגמאות.

הדוגמא המרכזית, האבטיפוס, נותן ההשראה לכל המושג הזה, היא קבוצת המספרים הטבעיים, {% equation %}\mathbb{N}{% endequation %} עם יחס הסדר הרגיל עליה, כלומר {% equation %}0<1<2<3<\ldots{% endequation %}. זה בוודאי יחס סדר מלא, ואם ניקח תת-קבוצה לא ריקה של טבעיים, האיבר הראשון שבה הוא בסך הכל האיבר המינימלי בגודלו. למשל, {% equation %}\left\{ 13,5,81\right\} {% endequation %} היא תת-קבוצה שכזו, והאיבר הראשון בה, על פי יחס הסדר, הוא 5.

זו תכונה שימושית בצורה יוצאת מן הכלל: הרבה הוכחות במתמטיקה כוללות אספקט שבו לוקחים תת-קבוצה כלשהי של טבעיים ואז מסתכלים על האיבר המינימלי בה. אפילו ההוכחה שהוכחות באינדוקציה עובדות היא כזו: כזכור, הוכחה באינדוקציה אומרת שאם טענה {% equation %}P{% endequation %} כלשהי מתקיימת עבור 0 (מסמנים זאת {% equation %}P\left(0\right){% endequation %}) ובנוסף, אם היא מתקיימת עבור טבעי {% equation %}n{% endequation %} כלשהו היא מתקיימת גם עבור {% equation %}n+1{% endequation %} ({% equation %}P\left(n\right)\Rightarrow P\left(n+1\right){% endequation %}) אז נובע מכך שהיא מתקיימת לכל הטבעיים ({% equation %}\forall n\in\mathbb{N}:P\left(n\right){% endequation %}). איך מוכיחים את זה? פשוט, מסתכלים על קבוצת הטבעיים שעבורם {% equation %}P{% endequation %} אינה מתקיימת; אם היא ריקה, סיימנו, ואחרת קיים לה איבר ראשון, {% equation %}n{% endequation %}. מכיוון ש-{% equation %}P\left(0\right){% endequation %} אז {% equation %}n>0{% endequation %} ולכן גם {% equation %}n-1\in\mathbb{N}{% endequation %}, אבל מהמינימליות של {% equation %}n{% endequation %} עולה ש-{% equation %}P\left(n-1\right){% endequation %}, ועכשיו אפשר להסיק מכך שגם {% equation %}P\left(\left(n-1\right)+1\right)=P\left(n\right){% endequation %} - סתירה להנחה ש-{% equation %}P\left(n\right){% endequation %} לא מתקיים.

אפשר לשאול, ובצדק, מה בהוכחה שהראיתי כאן התבסס באופן ספציפי על המספרים הטבעיים - לכאורה בשינויים קלים ההוכחה תעבוד לכל קבוצה סדורה היטב. ובכן, בדיוק כך! הנה לנו אחת מהסיבות שבגללן אנחנו אוהבים קבוצות סדורות היטב. עוד אחזור לזה בהמשך.

בואו נתבונן כעת על הקבוצה {% equation %}\mathbb{Z}=\left\{ \ldots,-2,-1,0,1,2,\ldots\right\} {% endequation %} של המספרים השלמים. הקבוצה הזו סדורה בסדר מלא, אבל הוא <strong>לא</strong> סדר טוב, כי אפילו לכל {% equation %}\mathbb{Z}{% endequation %} עצמה אין איבר ראשון. אותה בעיה תמנע גם מ-{% equation %}\mathbb{Q}{% endequation %} להיות סדורה בסדר טוב. אבל מה קורה אם נפטרים מהבעיה הזו? למשל, בואו נסתכל על {% equation %}\mathbb{Q}^{\ge0}=\left\{ q\in\mathbb{Q}\ |\ q\ge0\right\} {% endequation %}. לקבוצה הזו בוודאי יש איבר ראשון: 0. לרוע המזל, זה לא מספיק בשביל שהקבוצה תהיה סדורה בסדר טוב, כי צריך שיהיה איבר ראשון <strong>לכל</strong> תת-קבוצה לא ריקה של {% equation %}\mathbb{Q}^{\ge0}{% endequation %}, והנה דוגמא לתת-קבוצה כזו שאין לה איבר ראשון (אני מסדר את אבריה כך שהגדול ביותר בא תחילה): {% equation %}\left\{ 1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\frac{1}{5},\ldots\right\} {% endequation %}. הקבוצה הזו "שואפת לאפס" באיזה מובן אינטואיטיבי, אבל מכיוון ש-0 אינו שייך אליה, אין לתת-הקבוצה הזו איבר ראשון. שימו לב לניואנס הזה: אם {% equation %}B\subseteq A{% endequation %} אז צריך שיהיה ל-{% equation %}B{% endequation %} איבר ראשון <strong>בתוך </strong>{% equation %}B{% endequation %} עצמה. לא משנה אם קיים ב-{% equation %}A\backslash B{% endequation %} מישהו שנראה כמו אינפימום של {% equation %}B{% endequation %}.

מה שכן אפשר לעשות הוא לקחת קבוצה קיימת ולהתעלל במושג הסדר הרגיל שלה - להחליף אותו במשהו שאולי נראה לנו ממש מוזר, אבל הוא כן יהיה סדר טוב. למשל, בואו נסתכל על {% equation %}\mathbb{Z}{% endequation %} ונגדיר שכל מספר <strong>שלילי</strong> יותר גדול מכל מספר <strong>חיובי</strong>, ובנוסף את השליליים אני מסדר לפי הערך המוחלט שלהם. במילים אחרות, נקבל את {% equation %}\mathbb{Z}=\left\{ 0,1,2,3,\ldots,-1,-2,-3,\ldots\right\} {% endequation %}, כשכאן אני כותב את האיברים משמאל לימין על פי הסדר שלהם. הקבוצה הזו <strong>כן</strong> סדורה היטב.

גם את {% equation %}\mathbb{Q}^{\ge0}{% endequation %} אפשר לסדר די בקלות בסדר טוב, וזה בעצם מה שעושים בהוכחה הסטנדרטית ש-{% equation %}\mathbb{Q}{% endequation %} בת מניה: אנחנו כותבים סדר כמו {% equation %}\frac{0}{0},\frac{0}{1},\frac{1}{0},\frac{0}{2},\frac{1}{1},\frac{2}{0},\ldots{% endequation %} - זה משהו די מגוחך שכולל איברים לא הגיוניים כמו {% equation %}\frac{0}{0}{% endequation %}, אבל העיקרון ברור - מהרשימה הזו אנחנו לוקחים רק את המספרים של {% equation %}\mathbb{Q}^{\ge0}{% endequation %}, בפעם הראשונה שהם הופיעו, והרשימה עצמה מסודרת כך: ראשית מופיעים כל הביטויים {% equation %}\frac{a}{b}{% endequation %} עם {% equation %}a,b\ge0{% endequation %} כך ש-{% equation %}a+b=0{% endequation %}; אחר כך כל הביטויים כך ש-{% equation %}a+b=1{% endequation %} וכן הלאה, כשבכל פעם אנחנו מתחילים מ-{% equation %}a=0{% endequation %} ומגדילים אותו תוך שאנו מקטינים את {% equation %}b{% endequation %} בהדרגה. זה יניב לנו את

{% equation %}\mathbb{Q}^{\ge0}=\left\{ 0,1,\frac{1}{2},2,\frac{1}{3},3,\ldots\right\} {% endequation %} 

זו קבוצה די מבולגנת, אבל אם חושבים על זה קצת, היא בעצם לא שונה במבנה שלה מהמספרים הטבעיים: פורמלית, נראה בהמשך שהיא <strong>איזומורפית</strong> אליהם. לעומת זאת, {% equation %}\mathbb{Z}=\left\{ 0,1,2,3,\ldots,-1,-2,-3,\ldots\right\} {% endequation %} לא איזומורפית: האיבר {% equation %}-1{% endequation %} בקבוצה הזו נטול קודם מיידי (איבר שקטן ממנו ואין איברים אחרים ביניהם) אבל ב-{% equation %}\mathbb{N}{% endequation %} עם יחס הסדר הרגיל זה לא קיים.

אם כן, בואו נדבר על איזומורפיזמים.

<h2>איזומורפיזם של קבוצות סדורות היטב - חימום</h2>

באופן כללי במתמטיקה, איזומורפיזם של שתי קבוצות אומר שהן אותו דבר עד כדי שינוי שמות - כש"אותו הדבר" צריך להתייחס גם ל<strong>מבנה</strong> הרלוונטי שיש על הקבוצות בהקשר שעליו מדברים. אם אין שום מבנה, אז איזומורפיזם {% equation %}f:A\to B{% endequation %} של קבוצות הוא בסך הכל פונקציה חח"ע ועל ביניהן; אבל בהקשר שלנו, שבו יש יחסי סדר על הקבוצות שאסמן {% equation %}\le_{A},\le_{B}{% endequation %}, איזומורפיזם הוא פונקציה {% equation %}f:A\to B{% endequation %} שהיא חח"ע, על ו<strong>משמרת סדר</strong>: כלומר, {% equation %}a\le b{% endequation %} אם ורק אם {% equation %}f\left(a\right)\le f\left(b\right){% endequation %}.

הנה דוגמא פשוטה. בואו נסדר את {% equation %}\mathbb{Z}{% endequation %} כך שמספרים חיוביים ושליליים מגיעים זה אחר זה: {% equation %}\mathbb{Z}=\left\{ 0,1,-1,2,-2,3,-3,\ldots\right\} {% endequation %}. עם הסדר הזה, {% equation %}\mathbb{Z}{% endequation %} היא בסך הכל {% equation %}\mathbb{N}{% endequation %} בתחפושת. הנה האיזומורפיזם המפורש: 

{% equation %}f\left(n\right)=\begin{cases} k & n=2k-1\\ -k & n=2k \end{cases}{% endequation %}

ההגדרה הזו עובדת לקבוצות סדורות באופן כללי, ואנחנו מסמנים {% equation %}A\cong B{% endequation %} כדי לציין ששתי הקבוצות הן איזומורפיות. מה שמעניין אותנו בהקשר של קבוצות סדורות היטב הוא שאיזומורפיזם מאפשר לנו <strong>להשוות</strong> בין קבוצות סדורות היטב שונות. במובן מסויים, לכל שתי קבוצות סדורות היטב, או ששתיהן איזומורפיות זו לזו, או שאחת מהן "גדולה יותר" ואז השניה איזומורפית לחלק ממנה, אבל לא סתם חלק - <strong>קטע התחלתי</strong>, שזה מושג חדש שאני צריך להגדיר אבל הוא די אינטואיטיבי: 

אם {% equation %}\left(A,<\right){% endequation %} היא קבוצה סדורה היטב ו-{% equation %}a\in A{% endequation %} אז <strong>הקטע ההתחלתי</strong> שמתאים ל-{% equation %}a{% endequation %} הוא הקבוצה {% equation %}a^{<}\triangleq\left\{ b\in A\ |\ b<a\right\} {% endequation %}, כלומר כל האיברים של {% equation %}A{% endequation %} שקטנים מ-{% equation %}a{% endequation %} עצמו (<strong>לא כולל</strong> {% equation %}a{% endequation %} עצמו, מה שיהיה רלוונטי מאוד בהוכחות שתכף נראה).

אני רוצה להוכיח שאם {% equation %}A,B{% endequation %} הן שתי קבוצות סדורות היטב, אז או ש-{% equation %}A\cong B{% endequation %}, או ש-{% equation %}A\cong b^{<}{% endequation %} לאיזה {% equation %}b\in B{% endequation %}, או ש-{% equation %}B\cong a^{<}{% endequation %} לאיזה {% equation %}a<A{% endequation %}. בגלל שזו הוכחה לא טריוויאלית מחלקים אותה לשלבים של טענות פשוטות יותר.

ראשית, נוכיח שאם {% equation %}A{% endequation %} סדורה היטב, אז היא <strong>לא</strong> איזומורפית לאף קטע התחלתי של עצמה, ואפילו יותר מזה - היא לא איזומורפית לאף תת-קבוצה של קטע התחלתי של עצמה. כלומר, ניקח {% equation %}a\in A{% endequation %} כלשהו ונוכיח שלכל {% equation %}B\subseteq a^{<}{% endequation %} מתקיים {% equation %}A\not\cong B{% endequation %}ֲ. נניח בשלילה שדווקא כן {% equation %}A\cong B{% endequation %} עבור {% equation %}B\subseteq a^{<}{% endequation %} כלשהי, עם איזומורפיזם {% equation %}f:A\to B{% endequation %}, ונשאל את עצמנו את השאלה - אל מי {% equation %}f{% endequation %} מעבירה את {% equation %}a{% endequation %}? היא מעבירה אותו לאיבר ב-{% equation %}a^{<}{% endequation %}, כלומר למישהו שקטן מ-{% equation %}a{% endequation %}:

{% equation %}f\left(a\right)<a{% endequation %}

עכשיו אני יכול להפעיל את {% equation %}f{% endequation %} על שני האגפים של אי השוויון הזה, ומכיוון ש-{% equation %}f{% endequation %} משמרת סדר, אני אקבל

{% equation %}f\left(f\left(a\right)\right)<f\left(a\right){% endequation %}

וככה אפשר להמשיך באופן כללי ולקבל

{% equation %}f^{n}\left(a\right)<f^{n-1}\left(a\right){% endequation %}

או במילים אחרות, קיבלתי סדרה יורדת אינסופית של איברים:

{% equation %}a>f\left(a\right)>f^{2}\left(a\right)>f^{3}\left(a\right)>\ldots{% endequation %}

בקבוצה סדורה היטב לא יכולה להיות סדרה כזו, כי אם נסתכל על הקבוצה {% equation %}\left\{ f^{n}\left(a\right)\ |\ n\in\mathbb{N}\right\} {% endequation %}, זו תת-קבוצה של {% equation %}A{% endequation %} ומכיוון ש-{% equation %}A{% endequation %} סדורה היטב, צריך להיות בה איבר ראשון, כזה שקטן מכל האיברים האחרים; אבל לכל איבר בסדרה הזו קיים איבר שקטן ממנו. הגענו לסתירה, והמסקנה היא ש-{% equation %}A\not\cong B{% endequation %}, כמו שרצינו.

הדבר השני שאני רוצה להוכיח בדרך אל המשפט הגדול הוא שאם {% equation %}A\cong B{% endequation %}, אז האיזומורפיזם ביניהם הוא <strong>יחיד</strong>. כלומר, אם {% equation %}f:A\to B{% endequation %} וגם {% equation %}g:A\to B{% endequation %} הם איזומורפיזמים, אז {% equation %}f=g{% endequation %}, או במילים אחרות: {% equation %}h=g^{-1}f=\text{Id}_{A}{% endequation %} הוא איזומורפיזם הזהות. 

ה-{% equation %}h{% endequation %} הזה הוא בעצם המפתח להוכחה: אם אנחנו לוקחים {% equation %}a\in A{% endequation %} אז {% equation %}h{% endequation %} היא בפרט איזומורפיזם בין הקבוצות {% equation %}a^{<}{% endequation %} ו-{% equation %}h\left(a\right)^{<}{% endequation %}. למה? ובכן, {% equation %}h{% endequation %} היא הרכבה של פונקציות חח"ע, על ושומרות סדר ולכן היא חח"ע, על ושומרת סדר בעצמה; עכשיו, אם {% equation %}x\in a^{<}{% endequation %} זה אומר ש-{% equation %}x<a{% endequation %}, ולכן {% equation %}h\left(x\right)<h\left(a\right){% endequation %} ומכאן ש-{% equation %}h\left(x\right)\in h\left(a\right)^{<}{% endequation %}; קיבלנו שהתמונה של {% equation %}a^{<}{% endequation %} על ידי {% equation %}h{% endequation %} מוכלת ב-{% equation %}h\left(a\right)^{<}{% endequation %}. מצד שני, אם {% equation %}y\in h\left(a\right)^{<}{% endequation %} אז {% equation %}y<h\left(a\right){% endequation %} ולכן {% equation %}h^{-1}\left(y\right)<a{% endequation %} ולכן המקור של {% equation %}y{% endequation %} שייך ל-{% equation %}a^{<}{% endequation %}. משני אלו נקבל שהתמונה של {% equation %}a^{<}{% endequation %} היא בדיוק {% equation %}h\left(a\right)^{<}{% endequation %} ולכן {% equation %}h{% endequation %} היא איזומורפיזם בין שתי הקבוצות הללו.

עכשיו, בואו נזכור ש-{% equation %}h{% endequation %} היא פונקציה מ-{% equation %}A{% endequation %} לעצמה: {% equation %}h:A\to A{% endequation %}. כלומר, {% equation %}a^{<}{% endequation %} וגם {% equation %}h\left(a\right)^{<}{% endequation %} שניהם קטעים התחלתיים של {% equation %}A{% endequation %} עצמה, ולכן או ש-{% equation %}a=h\left(a\right){% endequation %} או ש<strong>אחד מהם הוא קטע התחלתי של השני</strong>. אבל המשפט הקודם שראינו הוא שקבוצה לא יכולה להיות איזומורפית לקטע התחלתי של עצמה, ולכן בהכרח {% equation %}a=h\left(a\right){% endequation %}. זה מתקיים לכל {% equation %}a\in A{% endequation %} ולכן נובע מכך ש-{% equation %}h{% endequation %} היא הזהות, כמו שרצינו.

<h2>איזומורפיזם של קבוצות סדורות היטב - המשפט המרכזי</h2>

הגענו להוכחה של הטענה המרכזית שלנו: שאם {% equation %}A,B{% endequation %} הן קבוצות סדורות היטב אז הן איזומורפיות או שאחת מהן איזומורפית לקטע התחלתי של השניה. זו לא הוכחה קשה במיוחד, אבל היא כן קצת טריקית בגלל הטכניקה שבה משתמשים בה, שלא דומה לדברים אחרים שיש בתורת הקבוצות הנאיבית עד השלב הזה.

ראשית, לפני שנתחיל את הדבר העיקרי, בואו נשים לב לשני דברים שלא הבהרתי בניסוח המשפט:

<ol> <li>רק אחד משלושת המקרים יכול להתקיים, כי אם שני מקרים מתקיימים בו זמנית אפשר לקבל סיטואציה של קבוצה שאיזומורפית לתת-קבוצה של קטע התחלתי של עצמה, וראינו שזה לא יכול לקרות. למשל, אם {% equation %}A\cong B{% endequation %} עם איזומורפיזם {% equation %}f{% endequation %} וגם {% equation %}A\cong b^{<}{% endequation %} עם עבור {% equation %}b\in B{% endequation %} עם איזומורפיזם {% equation %}g{% endequation %} אז הרכבת האיזומורפיזמים {% equation %}gf^{-1}{% endequation %} היא איזומורפיזם {% equation %}B\cong b^{<}{% endequation %} וזו סתירה. או למשל אם {% equation %}A\cong b^{<}{% endequation %} עם {% equation %}f{% endequation %} ו-{% equation %}B\cong a^{<}{% endequation %} עם {% equation %}g{% endequation %} אז נקבל פונקציה חח"ע ושומרת סדר מ-{% equation %}A{% endequation %} אל {% equation %}a^{<}{% endequation %}. היא לאו דווקא על {% equation %}a^{<}{% endequation %}, אבל היא על תת-קבוצה של {% equation %}a^{<}{% endequation %}, אז אנחנו מקבלים איזומורפיזם של {% equation %}A{% endequation %} עם תת-קבוצה של קטע התחלתי של עצמה.</li>


<li>האיזומורפיזם שכן קיים הוא יחיד - זה בדיוק מה שהוכחנו קודם עבור שתי קבוצות כלליות.</li>

</ol>

עכשיו בואו נעבור להוכחה עצמה. האינטואיציה היא שכדי לבנות איזומורפיזם בין שתי קבוצות סדורות היטב, מתבקש (אפילו בלתי נמנע) להתחיל מלהעביר את האיברים הראשונים של שתיהן אחד לשני, ואז את האיברים "הבאים בתור", כלומר את האיברים הראשונים בקבוצת "האיברים שטרם טיפלנו בהם" וכן הלאה, אבל זה ניסוח די מסורבל - בניה "בשלבים" כשיכולים להיות אינסוף שלבים - ולאו דווקא אינסוף בן מניה של שלבים. צריך למצוא דרך לטפל בהכל "בבת אחת".

אז הנה רעיון: בואו נדמיין שאנחנו כן מבצעים את הבנייה בשלבים הזו, ובשלב מסוים אנחנו מחליטים להעביר את {% equation %}a\in A{% endequation %} אל {% equation %}b\in B{% endequation %}. מה זה אומר? מכיוון שאנחנו בונים את ההעתקה שלנו באופן הדרגתי, זה אומר שכבר טיפלנו <strong>בכל</strong> האיברים שקטנים מ-{% equation %}a{% endequation %} ו<strong>בכל</strong> האיברים שקטנים מ-{% equation %}b{% endequation %} והעברנו אותם זה לזה. במילים אחרות, כבר בנינו את האיזומורפיזם {% equation %}a^{<}\cong b^{<}{% endequation %}, וכעת אנחנו מרחיבים אותו על ידי הוספת הכלל {% equation %}a\mapsto b{% endequation %} לאיזומורפיזם. אבל למה לדבר על "הוספת כלל"? בשביל מה למדנו תורת הקבוצות אם לא כדי ללמוד שאפשר לדבר על פונקציות פשוט בתור קבוצות של זוגות? ובכן, אם כבר בנינו את האיזומורפיזם {% equation %}f:a^{<}\to b^{<}{% endequation %}, בואו נוסיף אל {% equation %}f{% endequation %} את האיבר {% equation %}\left(a,b\right){% endequation %}!

כל זה טוב ויפה, אבל איפה אני נפטר מהעניין הזה של בניה בשלבים? ובכן, אני צריך שלבים רק אם יש לי תהליך שיש בו <strong>אפשרויות בחירה</strong> כלשהן, אבל אני טוען שאין לנו שום בחירה. לא בחרתי להעביר את {% equation %}a{% endequation %} אל {% equation %}b{% endequation %} כי ככה יצא בבניה הספציפית שלי; אני מעביר את {% equation %}a{% endequation %} אל {% equation %}b{% endequation %} כי {% equation %}b{% endequation %} הוא האיבר <strong>היחיד</strong> שעבורו מתקיים {% equation %}a^{<}\cong b^{<}{% endequation %}. זכרו את מה שראינו: אם {% equation %}a^{<}\cong b^{<}{% endequation %} אז פשוט <strong>לא ייתכן</strong> ש-{% equation %}a^{<}{% endequation %} יהיה איזומורפי לכל קטע התחלתי אחר של {% equation %}B{% endequation %} (כי קטע כזה יכיל או יוכל ב-{% equation %}b^{<}{% endequation %}) והאיזומורפיזם {% equation %}a^{<}\cong b^{<}{% endequation %} הוא <strong>יחיד</strong>, אז הוא לא תלוי באיזו {% equation %}f{% endequation %} ספציפית שבניתי עד כה.

זה מוביל אותי אל ההגדרה של {% equation %}f{% endequation %} שבה אנחנו הולכים להשתמש, שהיא לב ההוכחה:

{% equation %}f=\left\{ \left(a,b\right)\in A\times B\ |\ a^{<}\cong b^{<}\right\} {% endequation %}

הפונקציה הזו היא האיזומורפיזם שאנחנו רוצים. לאיזה מבין המקרים? לכולם! לפי מי מהם שנכון. אם למשל {% equation %}A\cong b^{<}{% endequation %}, זה אומר שנקבל את כל הזוגות {% equation %}\left(a,b\right){% endequation %} עם {% equation %}a\in A{% endequation %}; לא כל ה-{% equation %}b{% endequation %}-ים של {% equation %}B{% endequation %} יופיעו, וזה בסדר גמור. אם לעומת זאת {% equation %}a^{<}\cong B{% endequation %} אז זה אומר שכל ה-{% equation %}b{% endequation %}-ים כן יופיעו אבל לא כל ה-{% equation %}a{% endequation %}-ים, וזה עדיין בסדר גמור. הפונקציה עובדת בכל מקרה.

אבל קודם כל צריך להשתכנע שקבוצת הזוגות הזו היא באמת פונקציה, ופונקציה חח"ע ועל ושומרת סדר. למרבה המזל, כמעט הכל נובע מדברים שכבר הוכחנו.

מה זה אומר ש-{% equation %}f{% endequation %} היא פונקציה? ראשית, זה אומר שלכל {% equation %}a{% endequation %} בתחום שלה צריך להתאים {% equation %}b{% endequation %} מהטווח, אבל מכיוון שלא התחייבנו על מה התחום אין מה להוכיח פה - את התחום נגדיר בדיוק בתור

{% equation %}\text{dom}f\triangleq\left\{ a\in A\ |\ \exists b\in B:\left(a,b\right)\in f\right\} {% endequation %}

שנית, זה אומר שלכל {% equation %}a{% endequation %} מתאים רק {% equation %}b{% endequation %} <strong>יחיד</strong>, אבל זה קל, כי אם {% equation %}\left(a,b_{1}\right),\left(a,b_{2}\right)\in f{% endequation %} אז זה אומר ש-{% equation %}a\cong b_{1}^{<}{% endequation %} וגם {% equation %}a\cong b_{2}^{<}{% endequation %} ומכאן נובע {% equation %}b_{1}^{<}\cong b_{2}^{<}{% endequation %} וזו סתירה אלא אם {% equation %}b_{1}=b_{2}{% endequation %} כי כבר הוכחנו שקבוצה לא איזומורפית לקטע התחלתי שלה.

באותו אופן בדיוק מראים שאם {% equation %}\left(a_{1},b\right),\left(a_{2},b\right)\in f{% endequation %} אז {% equation %}a_{1}=a_{2}{% endequation %}, כלומר ש-{% equation %}f{% endequation %} חח"ע. וזה ש-{% equation %}f{% endequation %} היא על הוא שוב עניין של איך מגדירים, ספציפית כאן איך מגדירים את הטווח של {% equation %}f{% endequation %}, שפשוט נזהה עם התמונה שלה {% equation %}\left\{ b\in B\ |\ \exists a\in A:\left(a,b\right)\in f\right\} {% endequation %}.

אז בבניה שלנו ראינו כבר ש-{% equation %}f{% endequation %} היא פונקציה חח"ע ועל בין תת-קבוצה כלשהי של {% equation %}A{% endequation %} ותת-קבוצה כלשהי של {% equation %}B{% endequation %}. אבל מהן הקבוצות הללו? בתור התחלה אני רוצה להראות שאם איבר {% equation %}a\in A{% endequation %} שייך לתחום של {% equation %}f{% endequation %}, כך גם כל {% equation %}a^{\prime}<a{% endequation %}.

אם {% equation %}a\in\text{dom}f{% endequation %} אז קיים {% equation %}b{% endequation %} כך ש-{% equation %}a^{<}\cong b^{<}{% endequation %}. בואו נסמן את האיזומורפיזם הזה ב-{% equation %}g{% endequation %}: {% equation %}g:a^{<}\to b^{<}{% endequation %}. עכשיו, בואו נסתכל על {% equation %}\left(a^{\prime}\right)^{<}{% endequation %}: זו תת-קבוצה של {% equation %}a^{<}{% endequation %} ולכן אפשר <strong>לצמצם</strong> את האיזומורפיזם {% equation %}g{% endequation %} לתת-הקבוצה הזו. אם נסמן {% equation %}b^{\prime}=g\left(a^{\prime}\right){% endequation %} נקבל שהצמצום הזה נותן לנו איזומורפיזם {% equation %}\left(a^{\prime}\right)^{<}\cong\left(b^{\prime}\right)^{<}{% endequation %} (הוא בהכרח תופס את כל האיברים ב-{% equation %}\left(b^{\prime}\right)^{<}{% endequation %} כי איבר שגדול או שווה ל-{% equation %}a^{\prime}{% endequation %} לא יכול לעבור למשהו שקטן מ-{% equation %}b^{\prime}{% endequation %}).

כלומר, ראינו שאם {% equation %}\left(a,b\right)\in f{% endequation %} אז לכל {% equation %}a^{\prime}<a{% endequation %} קיים {% equation %}b^{\prime}<b{% endequation %} כך ש-{% equation %}\left(a^{\prime},b^{\prime}\right)\in f{% endequation %} (ובדומה לכל {% equation %}b^{\prime}<b{% endequation %} קיים {% equation %}a^{\prime}<a{% endequation %} מתאים). המסקנה מזה היא כפולה: ראשית, {% equation %}f{% endequation %} משמרת סדר. שנית, אם התחום של {% equation %}f{% endequation %} הוא לא כל {% equation %}A{% endequation %}, אז מכיוון ש-{% equation %}A{% endequation %} סדורה היטב אפשר להסתכל על {% equation %}A\backslash\text{dom}f{% endequation %} ולקבוצה הזו יהיה איבר ראשון, {% equation %}a{% endequation %}. לא ייתכן שיהיו איברים ב-{% equation %}\text{dom}f{% endequation %} שגדולים מ-{% equation %}a{% endequation %} אחרת מה שראינו כרגע היה מוכיח ש-{% equation %}a\in\text{dom}f{% endequation %}, ולכן המסקנה היא ש-{% equation %}\text{dom}f=a^{<}{% endequation %}. באותו האופן התמונה של {% equation %}f{% endequation %} היא או {% equation %}B{% endequation %} כולה או {% equation %}b^{<}{% endequation %} עבור {% equation %}b\in B{% endequation %} כלשהו.

אז אם לסכם, הראינו ש-{% equation %}f{% endequation %} היא פונקציה חח"ע, על ומשמרת סדר שהתחום שלה הוא {% equation %}A{% endequation %} או קטע התחלתי של {% equation %}A{% endequation %} והטווח שלה הוא {% equation %}B{% endequation %} או קטע התחלתי של {% equation %}B{% endequation %}: זה מכסה את כל האפשרויות ומסיים את ההוכחה.

<h2>בונוס: האם כל קבוצה ניתנת לסידור טוב?</h2>

התחלנו את הפוסט עם האבחנה ש-{% equation %}\mathbb{Z}{% endequation %} ו-{% equation %}\mathbb{Q}{% endequation %} עם הסדר "הרגיל" עליהן אינן סדורות בסדר טוב, אבל אפשר איכשהו להתחכם וכן להגדיר עליהן סדרים טובים (אפילו כמה סדרים טובים שונים). האופן שבו עשיתי את זה היה מאוד <strong>ספציפי</strong> לקבוצות הללו; השתמשתי בהתחכמויות שנעזרות במבנה שכבר קיים עליהן. אם אני אצטרך לעשות משהו דומה עם {% equation %}\mathbb{R}{% endequation %}, האם אוכל למצוא התחכמות דומה? ובכן, לא. <strong>אין לי מושג</strong> איך לסדר את {% equation %}\mathbb{R}{% endequation %} בסדר טוב. זה תרגיל טוב לנסות ולעשות את זה בצורה קונסטרוקטיבית, כי לנסות ולהיתקע (או לא לדעת מאיפה להתחיל בכלל) בעצמכם זה יותר משכנע מאשר שאני סתם אגיד "אני לא יודע".

עדיין, כמה מסובך סדר טוב יכול להיות? מה קשה בלהגיד "ניקח איבר כלשהו של {% equation %}\mathbb{R}{% endequation %}, זה יהיה האיבר הראשון שלנו, עכשיו ניקח עוד איבר והוא יהיה השני וכן הלאה"? ובכן, מי מבטיח לנו שבסופו של דבר נמצה באופן הזה את <strong>כל</strong> האיברים של {% equation %}\mathbb{R}{% endequation %}? הרי יש <a href="https://gadial.net/2020/10/28/diagonalizations_and_infinite_sets/">מספר לא בן מניה שלהם</a>. אנחנו צריכים איכשהו לטפל בכל האיברים בבת אחת, וזה למרות שבניגוד לבניה של האיזומורפיזם מהחלק הקודם, כאן הבניה מאוד תלויה <strong>בבחירות</strong> שביצענו בדרך. כאן נחלצת לעזרתנו <strong>אקסיומת הבחירה</strong>.

הזכרתי את אקסיומת הבחירה <a href="https://gadial.net/2020/06/20/general_cartesian_products/">בפוסט על מכפלות קרטזיות כלליות</a>, בואו נזכיר אותה שוב, בניסוח שהכי נוח לי כאן: אם {% equation %}X{% endequation %} היא משפחה של קבוצות לא ריקות ({% equation %}A\ne\emptyset{% endequation %} לכל {% equation %}A\in X{% endequation %}) אז קיימת {% equation %}f:X\to\bigcup_{A\in X}A{% endequation %} ("פונקציית בחירה") כך שלכל {% equation %}A\in X{% endequation %} מתקיים {% equation %}f\left(A\right)\in A{% endequation %}. אנחנו קוראים לזה "אקסיומה" כי אי אפשר להוכיח את זה מיתר <a href="https://gadial.net/2019/10/20/zf_axioms_intro/">האקסיומות של צרמלו פרנקל</a>; האקסיומות הללו נותנות לנו סט כלים מוגבל יחסית בשביל לבנות קבוצות, כדי למנוע סיטואציה שבה אנחנו בונים בטעות קבוצה פרדוקסלית, ופונקציות בחירה הן קבוצות מורכבות מאוד לעתים, כאלו שפשוט לא ניתן לבנות עם סט הכלים המוגבל של צרמלו-פרנקל.

אם אנחנו מניחים את אקסיומת הבחירה, אז די פשוט להוכיח שכל קבוצה {% equation %}A{% endequation %} ניתנת לסידור בסדר טוב. ראשית, נסתכל על אוסף כל תת-הקבוצות הלא ריקות של {% equation %}A{% endequation %} (פורמלית, {% equation %}X=\mathcal{P}\left(A\right)\backslash\left\{ \emptyset\right\} {% endequation %}) וניקח פונקציית בחירה {% equation %}f{% endequation %} על האוסף הזה, כלומר נניח שיש לנו פונקציה שמקבלת תת-קבוצה לא ריקה {% equation %}B\subseteq A{% endequation %} ומחזירה {% equation %}f\left(B\right)=b\in B{% endequation %}.

סליחה, אמרתי "די פשוט"? האמת שזה לא כזה פשוט. גם עם פונקציית הבחירה לצידנו, לנסות ולחשוב מה הצעד הבא זה לא קל במיוחד. דרך אחת היא להמשיך עם הגישה של הגדרה "רקורסיבית", באמצעות כלי שנקרא <strong>רקורסיה על-סופית</strong>. זה בדיוק מה שעשיתי <a href="https://gadial.net/2012/06/04/choice_order_zorn/">בפוסט שכתבתי בעבר</a> על השקילות בין משפט הסדר הטוב ואקסיומת הבחירה. שם המחיר היה לא רק שימוש ברקורסיה על-סופית אלא גם נפנוף ידיים כללי, ולכן יכול להיות נחמד להציג כאן הוכחה שתהיה פורמלית לגמרי ולא תזדקק לכל זה, אבל המחיר יהיה טיפה מאמץ שהיא תדרוש מאיתנו (אפשר גם להשתמש במשהו אחר, שנקרא "הלמה של צורן", שהוא נפלא בפני עצמו אבל לדבר עליו יצריך אותי להכניס עוד סט חדש של מושגים שאני לא צריך כאן, במחיר של זה שההוכחה תהיה דומה מאוד לשימוש בלמה של צורן).

הנה ההגדרה המרכזית שנזדקק לה: נאמר שלקבוצה {% equation %}B\subseteq A{% endequation %} יש את "תכונה X" אם <strong>קיים</strong> סדר טוב של {% equation %}B{% endequation %} כך שלכל {% equation %}b\in B{% endequation %} מתקיים {% equation %}f\left(A\backslash b^{<}\right){% endequation %}. במילים אחרות, אם {% equation %}f{% endequation %} מגדירה לנו סדר טוב על {% equation %}B{% endequation %} בצורה הנחמדה שאנחנו מצפים לה: בהינתן כל האיברים שסידרנו עד כה, נבקש מ-{% equation %}f{% endequation %} "תני לנו איבר מ-{% equation %}A{% endequation %} שטרם סידרנו", היא תחזיר לנו את {% equation %}b{% endequation %} והוא יהיה האיבר הבא בסדר (ולכן קבוצת האיברים שסידרנו עד שהגענו אל {% equation %}b{% endequation %} היא בדיוק {% equation %}b^{<}{% endequation %}). שימו לב שזו לא הגדרה "תהליכית" כך שאנחנו לא צריכים לדבר על רקורסיות על סופיות ושאר ירקות, אבל מצד שני אם נוכיח של-{% equation %}A{% endequation %} עצמה יש את תכונה X, ניצחנו.

האם בכלל יש קבוצות שמקיימות את תכונה X? ובכן, {% equation %}\emptyset{% endequation %} מקיימת אותה באופן ריק, פשוט כי תכונה X מנוסחת בתור "לכל {% equation %}b\in B{% endequation %}..." וב-{% equation %}\emptyset{% endequation %} אין איברים ואפשר "לסדר אותה בסדר טוב" ריק.

בנוסף, לכל קבוצה {% equation %}B\subset A{% endequation %} ששונה מ-{% equation %}A{% endequation %} ומקיימת את תכונה X, אפשר להרחיב אותה באופן טבעי כך שתמשיך לקיים את תכונה X: נבנה את {% equation %}B\cup\left\{ f\left(A\backslash B\right)\right\} {% endequation %}, כלומר, נבקש את האיבר "הבא בתור" מ-{% equation %}f{% endequation %}, ונרחיב את הסדר הטוב על {% equation %}B{% endequation %} כך שהאיבר הזה יהיה האחרון.

שני אלו מראים לנו שיש כנראה כמות יפה של קבוצות שמקיימות את תכונה X, אז אפשר לעשות תעלול סטנדרטי ולהסתכל על <strong>האיחוד</strong> שלהן, שאסמן בתור {% equation %}C\subseteq A{% endequation %}. אם גם {% equation %}C{% endequation %} מקיימת את תכונה X, ניצחנו; ינבע מכך ש-{% equation %}C=A{% endequation %}. למה? כי אם {% equation %}C\ne A{% endequation %} אז אפשר <strong>להרחיב</strong> אותה כפי שראינו קודם ולקבל קבוצה שמכילה ממש את {% equation %}C{% endequation %} אבל <strong>השתתפה באיחוד </strong>שנתן את {% equation %}C{% endequation %} מלכתחילה, וזו כמובן סתירה.

אז האתגר שלנו הוא להסתכל על איחוד של קבוצות שמקיימות את תכונה X ולהראות שגם הוא מקיים את תכונה X (מי שמכירות את הלמה של צורן כנראה ממלמלות עכשיו "כל זה נשמע מוכר באופן חשוד" או משהו).

מה שאני ארצה להראות הוא שאין לקבוצות הרבה גמישות בבואן לקיים את תכונה X; הפונקציה {% equation %}f{% endequation %} מכריחה באופן די קשוח כל קבוצה כזו להשתמש בסדר טוב ספציפי. בניסוח קונקרטי, אם {% equation %}B_{1},B_{2}\subseteq A{% endequation %} הן שתי קבוצות סדורות בסדר טוב שמקיימות את תכונה X ביחס לסדר הטוב הזה, כך ש-{% equation %}B_{1}\cong B_{2}{% endequation %}, אז {% equation %}B_{1}=B_{2}{% endequation %} והאיזומורפיזם שלהן הוא הזהות. כלומר, אין כזה דבר, שני סדרים טובים שונים (בין אם על אותה קבוצה ובין אם על קבוצות אחרות) שמאפשרים לקבוצה לקיים את תכונה X.

ההוכחה די פשוטה: ניקח את האיזומורפיזם {% equation %}g:B_{1}\to B_{2}{% endequation %} ונניח שהוא לא פונקציית הזהות, אז יהא {% equation %}b\in B_{1}{% endequation %} האיבר הראשון מבין אלו שמקיימים {% equation %}b\ne g\left(b\right){% endequation %}. המשמעות היא ש-{% equation %}b^{<}=g\left(b\right)^{<}{% endequation %} (כי כל האיברים שקטנים מ-{% equation %}b{% endequation %} עוברים לעצמם בגלל המינימליות של {% equation %}b{% endequation %}).

עכשיו, מכיוון ש-{% equation %}B_{1},B_{2}{% endequation %} מקיימות את תכונת X, המשמעות של זה היא ש-

{% equation %}b=f\left(B_{1}\backslash b^{<}\right)=f\left(B_{1}\backslash g\left(b\right)^{<}\right)=g\left(b\right){% endequation %}

וזו סתירה להנחה ש-{% equation %}b\ne g\left(b\right){% endequation %}, אז קיבלנו ש-{% equation %}g{% endequation %} היא אכן הזהות.

מה אפשר להסיק מכך? קחו שתי קבוצות {% equation %}B_{1},B_{2}\subseteq A{% endequation %} כלשהן שמקיימות את תכונה X. שתיהן סדורות בסדר טוב כלשהו; המשפט המרכזי שהצגנו קודם אומר שהן או איזומורפיות, או שאחת מהן איזומורפית לקטע התחלתי של השניה. אבל כפי שראינו, בסיטואציה הספציפית שלנו עם תכונה X, אין "איזומורפיזם". יש רק שוויון. או ש-{% equation %}B_{1}=B_{2}{% endequation %}, או שאחת מהן היא קטע התחלתי של השניה. במילים אחרות, כל הקבוצות הללו סדורות <strong>באותו סדר טוב</strong>.

עכשיו, מה זה סדר טוב? בסופו של דבר זה יחס - קבוצה של זוגות. אם ניקח מכל קבוצה עם תכונה X את הסדר הטוב שלה ונאחד את כל הסדרים הטובים הללו, התוצאה תהיה סדר טוב על איחוד כל הקבוצות הללו, {% equation %}C{% endequation %}. כדי לראות שהסדר הזה מקיים את תכונה X, פשוט ניקח {% equation %}c\in C{% endequation %} כלשהו; הוא שייך לאחת מקבוצות ה-X שבאיחוד, והקבוצה הזו כבר מראה שהוא מקיים {% equation %}c=f\left(A\backslash c^{<}\right){% endequation %}. סיימנו!

<h2>מה הלאה?</h2>

בכל הדיון שלנו על קבוצות סדורות היטב חזר שוב ושוב עניין ה"איזומורפיזם" שלהן. במקום שבו יש לי איזומורפיזמים, עולה השאלה האם יש לי אובייקטים "קנוניים" שיכולים לייצג לי את המחלקות השונות של אובייקטים איזומורפיים. אם הולכים בגישה הזו מגיעים חיש קל אל מה שנקרא <strong>סודרים</strong>, שהוא המושג הבא שנדבר עליו. 