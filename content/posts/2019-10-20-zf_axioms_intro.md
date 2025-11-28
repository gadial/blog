---
title: "מפגש ראשון עם אקסיומות צרמלו-פרנקל"
layout: post
categories:
  - תורת הקבוצות
tags:
  - תורת הקבוצות
  - צרמלו-פרנקל
social_media_share: true
---

את <a href="https://gadial.net/2019/10/19/what_is_set_theory/">הפוסט הקודם שלי</a> על תורת הקבוצות סיימתי בהצגת הפרדוקס של ראסל, שהוא מעין תמרור אזהרה בשבילנו - אי אפשר סתם להגדיר קבוצות איך שבא לנו, זה מוביל בקלות לפרדוקסים במתמטיקה. לשאלה "איך פותרים את זה" אין תשובה חד משמעית - צצו כל מני גישות במתמטיקה להתמודדות עם הבעיה הזו, אבל מכיוון שאני לא רוצה להתעסק בפרדוקס של ראסל אלא בתורת הקבוצות כפי שכיום עוסקים בה במתמטיקה אני אתאר רק את הפתרון המקובל ביותר כיום - <strong>אקסיומות צרמלו-פרנקל</strong>, או בקיצור ZF.

כדי להגדיר במפורש את צרמלו-פרנקל או לדבר בכלל על מה זו המשמעות של אקסיומות כאלו אני צריך לוגיקה מתמטית, וזה מקפיץ את הפוסטים הללו מרמת "מתמטיקה בסיסית" לרמת "מתמטיקה בסיסית פחות" ואני עדיין לא רוצה ללכת לשם, אז בואו נחכה עם הדיון הפורמלי עד שנגיע לתורת הקבוצות האקסיומטית, אי שם בעתיד. עם זאת, אני לא רוצה לוותר על הצגה לא פורמלית של צרמלו-פרנקל כי זה מעניין וכי כדאי שנתרגל. <strong>לא אציג כרגע את כל האקסיומות</strong>, אבל אציג מספיק מהן כדי שיהיה מעניין ואל מה שהושמט נחזור בעתיד.

הפוסט הזה עלול להיות קשה יחסית, כך שאפשר לדלג עליו או על חלקים ממנו אם נתקעים בהם, ואולי כדאי לחזור אליו אחר כך כדי להבין כמה מהנקודות העדינות שאני מתאר. אני לא הולך לבנות בו משהו שלא יתואר במפורש בפוסטים אחרים אבל הוא כן יתן מסגרת של "למה אפשר לעשות את מה שאנחנו עושים" שלא ארחיב עליה באותה מידה בהמשך, עד שלא נגיע אל תורת הקבוצות האקסיומטית.

נתחיל עם השאלה "מתי שתי קבוצות הן שוות?" שדיברנו עליה בפוסט הקודם. אמרתי ש-{% equation %}A=B{% endequation %} אם ורק אם {% equation %}a\in A\iff a\in B{% endequation %} - במילים אחרות, אם לשתי קבוצות יש את אותם האיברים, הן שוות (אין "מידע נוסף" על קבוצות, כמו למשל השם שלהן או צבע או וואטאבר שמאפשר להבדיל ביניהן). זו אחת מאקסיומות צרמלו-פרנקל: <strong>אקסיומת ההיקפיות</strong>.

בואו נציג הגדרה וסימון שהם שימושיים בכל חלקי המתמטיקה: אני אומר ש-{% equation %}A{% endequation %} היא <strong>תת-קבוצה</strong> של {% equation %}B{% endequation %} ומסמן את זה בתור {% equation %}A\subseteq B{% endequation %} אם {% equation %}a\in A\Rightarrow a\in B{% endequation %}, כלומר אם כל איבר של {% equation %}A{% endequation %} הוא גם איבר של {% equation %}B{% endequation %}. לפעמים אני אגיד ש-{% equation %}B{% endequation %} <strong>מכילה</strong> את {% equation %}A{% endequation %}, וזה כבר פתח לבלבול: האינטואיציה היא לפעמים שאם {% equation %}B{% endequation %} "מכילה" את {% equation %}A{% endequation %} זה אומר ש-{% equation %}A{% endequation %} הוא איבר של {% equation %}B{% endequation %}, אבל זה בהחלט לא המצב. למשל, {% equation %}\left\{ 1,7\right\} \subseteq\left\{ 1,7,17\right\} {% endequation %} אבל {% equation %}\left\{ 1,7\right\} {% endequation %} אינה איבר של {% equation %}\left\{ 1,7,17\right\} {% endequation %}. כדי להגיד {% equation %}A\in B{% endequation %} אני אגיד ש-{% equation %}A{% endequation %} <strong>שייכת</strong> ל-{% equation %}B{% endequation %}; למיטב ידיעתי זו הטרמינולוגיה הסטנדרטית בעברית.

עכשיו אפשר לנסח את אקסיומת ההיקפיות בעזרת הסימון החדש שלנו: {% equation %}A=B{% endequation %} אם ורק אם {% equation %}A\subseteq B{% endequation %} וגם {% equation %}B\subseteq A{% endequation %}. זה פשוט ניסוח אחר של אקסיומת ההיקפיות, אבל הוא גם "שיטת העבודה" הסטנדרטית במתמטיקה כשרוצים להוכיח שוויון קבוצות - מוכיחים הכלה דו-כיוונית שכזו. המון הוכחות במתמטיקה הן פשוט הוכחות הכלה דו-כיוונית.

אחרי שהסכמנו על מהי קבוצה, בערך, אפשר להתחיל לבנות את היקום של תורת הקבוצות. אז בואו נתחיל כמו בפוסט הקודם, מהקבוצה הריקה: {% equation %}\emptyset{% endequation %}. אני אניח שקבוצה כזו קיימת - זו תהיה <strong>אקסיומת הקבוצה הריקה</strong> של צרמלו-פרנקל (בהמשך נראה שאפשר להסיק אותה מאקסיומות אחרות של צרמלו-פרנקל אבל אני ממש לא רוצה לאפטמז דברים כאן). שימו לב שאני מדבר על <strong>ה</strong>קבוצה <strong>ה</strong>ריקה, בה' הידיעה - יש כאן הנחה מתמטית סמויה לפיה קיימת רק קבוצה ריקה <strong>אחת</strong> - אבל זה נובע מיידית מאקסיומת ההיקפיות. עוד נקודה מעניינת שנוגעת לקבוצה הריקה היא שמתקיים {% equation %}\emptyset\subseteq A{% endequation %} לכל קבוצה {% equation %}A{% endequation %}. למה? ובכן, זו דוגמא למה שנקרא במתמטיקה <strong>נכון באופן ריק</strong>. הטענה {% equation %}\emptyset\subseteq A{% endequation %}, על פי הגדרה, היא בעצם הטענה {% equation %}a\in\emptyset\Rightarrow a\in A{% endequation %}. צד שמאל של הגרירה לא מתקיים אף פעם, לאף {% equation %}a{% endequation %}, ולכן צד ימין של הגרירה אף פעם לא "עומד למבחן". באופן כללי כשיש לי טענה של גרירה שבה התנאי אף פעם לא מתקיים אני אומר שהטענה הזו נכונה באופן ריק.

כזכור, אני רוצה לשכנע אתכם שאפשר לבנות את "כל המתמטיקה" מתוך מושג הקבוצה. הדבר הראשון שאני רוצה לבנות הוא את המספרים הטבעיים. כבר אמרתי בפוסט הקודם ש-{% equation %}0\triangleq\emptyset{% endequation %}, אז לפחות את {% equation %}0{% endequation %} בניתי. מה עם {% equation %}1{% endequation %}? הגדרתי אותו בתור {% equation %}1\triangleq\left\{ 0\right\} {% endequation %}. מה שמעלה את השאלה - האם הקבוצה {% equation %}\left\{ 0\right\} {% endequation %} קיימת? אני הרי כרגע נוקט בגישת "שום דבר לא קיים בלי שאפשר יהיה להוכיח את זה". כרגע אין לי אקסיומה שנותנת את זה. אז למה לא להוסיף? נאמר, נוסיף אקסיומה שאומרת שאם {% equation %}x{% endequation %} קיים, גם {% equation %}\left\{ x\right\} {% endequation %} קיים. זה לא כזה חזק ובוודאי לא יכול ליצור קבוצה הרסנית כמו בפרדוקס של ראסל שיש בה הרבה יותר מאיבר אחד. אם תהיה לי אקסיומה כזו, גם הקיום של 1 מובטח. האקסיומה הזו היא לא חלק מצרמלו-פרנקל; אוטוטו נבין מה יש במקומה. אבל בינתיים נזרום איתה.

אבל מה עם 2? הגדרתי {% equation %}2=\left\{ 0,1\right\} {% endequation %}. עכשיו, כבר יש לי את 0 ואת 1 אז על פי האקסיומה שתיארתי לפני רגע, גם הקבוצות {% equation %}\left\{ 0\right\} {% endequation %} ו-{% equation %}\left\{ 1\right\} {% endequation %} קיימות. עכשיו אני רוצה לטעון שקיימת קבוצה שכוללת גם את האיבר של {% equation %}\left\{ 0\right\} {% endequation %} וגם את האיבר של {% equation %}\left\{ 1\right\} {% endequation %}. לדבר כזה יש שם במתמטיקה: <strong>איחוד קבוצות</strong>.

בואו נגדיר את זה במפורש: אם {% equation %}A,B{% endequation %} הן קבוצות כלשהן, אז <strong>האיחוד</strong> שלהן הוא קבוצה שאבריה הם בדיוק אברי {% equation %}A{% endequation %} ו-{% equation %}B{% endequation %}. פורמלית ועם סימון:

{% equation %}A\cup B\triangleq\left\{ a\ |\ a\in A\vee a\in B\right\} {% endequation %}

כאשר {% equation %}\vee{% endequation %} הוא סימון מתמטי ל"או".

אם כבר הצגתי איחוד, בואו נציג גם את בן דודו <strong>חיתוך</strong>. חיתוך של שתי קבוצות הוא קבוצת האיברים שמשותפים לשתי הקבוצות הללו:

{% equation %}A\cap B\triangleq\left\{ a\ |\ a\in A\wedge a\in B\right\} {% endequation %}

כאשר {% equation %}\wedge{% endequation %} הוא סימון מתמטי ל"וגם".

הנה לנו שתי אקסיומות כיפיות: אם {% equation %}A,B{% endequation %} קיימות אז גם {% equation %}A\cup B{% endequation %} וגם {% equation %}A\cap B{% endequation %} קיימות. כמו קודם, אלו לא אקסיומות של צרמלו-פרנקל כי האקסיומה על האיחוד תוחלף במשהו חזק יותר (שבלעדיו אי אפשר לעשות דברים מעניינים) והאקסיומה על החיתוך תתגלה כמיותרת בהינתן אקסיומות שטרם הגעתי אליהן. אבל גם האקסיומות הללו לא יישארו איתנו לאורך זמן, המשמעות שלהן תישאר תמיד - אם הצלחנו להוכיח את הקיום של {% equation %}A,B{% endequation %} אנחנו מקבלים את הקיום של האיחוד והחיתוך שלהן במתנה.

זה נותן לנו את המספרים הטבעיים: כאמור, {% equation %}2=\left\{ 0\right\} \cup\left\{ 1\right\} {% endequation %}, וכמו כן {% equation %}3=\left\{ 0,1\right\} \cup\left\{ 2\right\} {% endequation %}, כלומר {% equation %}3=2\cup\left\{ 2\right\} {% endequation %}. באופן דומה {% equation %}4=3\cup\left\{ 3\right\} {% endequation %} ובאופן הכי כללי, {% equation %}n+1=n\cup\left\{ n\right\} {% endequation %}. זה מוכיח לנו שלכל {% equation %}n{% endequation %} טבעי, הקבוצה שקראתי לה {% equation %}n{% endequation %} אכן קיימת. וזה מוכיח שהמספרים הטבעיים קיימים... רגע, רגע, רגע. בואו לא נרוץ קדימה מהר מדי. עכשיו הגענו לנקודה מבלבלת שחשוב לשים על השולחן כבר עכשיו.

כזכור, מה שאנחנו קוראים לו במתמטיקה "המספרים הטבעיים" הוא הקבוצה {% equation %}\mathbb{N}\triangleq\left\{ 0,1,2,3,\dots\right\} {% endequation %}. אני חד משמעית <strong>לא הוכחתי</strong> שהקבוצה הזו קיימת. הוכחתי שכל איבר שלה קיים; זה <strong>לא אומר</strong> שקיימת קבוצה שמכילה את כל האיברים הללו. התעלול שעשיתי עם האקסיומה שבהינתן {% equation %}x{% endequation %} מייצרת את {% equation %}\left\{ x\right\} {% endequation %} ועם האיחוד לא נותן את זה; הוא מאפשר לי לבנות כל קבוצה <strong>סופית</strong>, אבל הוא לא מאפשר לי לבנות קבוצות <strong>אינסופיות</strong>.

אתם יכולים לטעון - רגע, מה הבעיה? נסתכל על האיחוד האינסופי {% equation %}\left\{ 0\right\} \cup\left\{ 1\right\} \cup\left\{ 2\right\} \cup\dots{% endequation %}. העניין הוא שלא הגדרתי "איחוד אינסופי" בשום מקום; המושג לא קיים ואין לי אקסיומה שמדברת עליו. הגדרתי איחוד שפועל על שתי איברים ותו לא. אפשר להרחיב פעולה על שני איברים לפעולה על {% equation %}n{% endequation %} איברים באופן אינדוקטיבי: למשל, {% equation %}A\cup B\cup C{% endequation %} זו דרך מקוצרת לכתוב {% equation %}\left(A\cup B\right)\cup C{% endequation %}; אבל עבור איחוד של אינסוף קבוצות זה חסר משמעות.

האם האקסיומות שיש לנו יכולות לבנות את {% equation %}\mathbb{N}{% endequation %} בדרך קצת יותר חכמה? לא אוכיח את זה כרגע, אבל <strong>לא</strong>. אני חייב אקסיומה נוספת כדי לקבל את {% equation %}\mathbb{N}{% endequation %} עצמה. לעת עתה בואו פשוט נניח ש-{% equation %}\mathbb{N}{% endequation %} קיימת וזו תהיה האקסיומה שלנו - היא נקראת <strong>אקסיומת האינסוף</strong>, מכיוון שהיא מוכיחה את הקיום של קבוצה אינסופית. יש לה עוד ניסוחים שונים ומשונים בתורת הקבוצות האקסיומטית אבל המשמעות של כולן היא אותה משמעות.

בואו נעשה סיכום ביניים של האקסיומות שיש לנו עד כה:

<ol> <li><strong>אקסיומת ההיקפיות</strong>: שתי קבוצות הן שוות אם הן בעלות אותם איברים: {% equation %}A=B{% endequation %} אם ורק אם {% equation %}a\in A\iff a\in B{% endequation %}.</li>


<li><strong>אקסיומת הקבוצה הריקה</strong>: הקבוצה {% equation %}\emptyset{% endequation %} קיימת.</li>


<li>אם האיבר {% equation %}a{% endequation %} קיים אז הקבוצה {% equation %}\left\{ a\right\} {% endequation %} קיימת.</li>


<li>אם {% equation %}A,B{% endequation %} קיימות אז {% equation %}A\cup B{% endequation %} קיימת ו-{% equation %}A\cap B{% endequation %} קיימת.</li>


<li><strong>אקסיומת האינסוף: </strong>{% equation %}\mathbb{N}{% endequation %} קיימת.</li>

</ol>

עכשיו שראינו אותן, אני רוצה לשנות את אקסיומות 3-4 כדי שיתאימו למה שיש בצרמלו-פרנקל. העניין הבסיסי שאני בא להתמודד איתו הוא שאני <strong>כן</strong> רוצה לדבר על איחודים אינסופיים. איחוד אינסופי הוא חלק מהותי מהמתמטיקה. אני לא יכול בלעדיו. אז נתחיל מלהגדיר אותו, אבל נגדיר אותו בצורה שבה אני עדיין יכול "לשלוט" על מה שקורה בו וזה לא מייצר לי קבוצות משוגעות.

בואו נניח ש-{% equation %}X{% endequation %} היא קבוצה שכל האיברים שלה הן קבוצות בעצמן - דבר כזה נקרא <strong>משפחה של קבוצות</strong>. אני אגדיר איחוד על כל האיברים של {% equation %}X{% endequation %}, ואסמן זאת {% equation %}\bigcup X{% endequation %}, באופן הבא: {% equation %}a{% endequation %} שייך ל-{% equation %}\bigcup X{% endequation %} אם <strong>קיימת</strong> קבוצה {% equation %}A\in X{% endequation %} כך ש-{% equation %}a\in A{% endequation %}. פורמלית, תוך שימוש בסימן {% equation %}\exists{% endequation %} שמתאר "קיים", אני מגדיר זאת כך:

{% equation %}\bigcup X=\left\{ a\ |\ \exists A\in X:a\in A\right\} {% endequation %}

עכשיו אפשר להציג את <strong>אקסיומת האיחוד</strong> של צרמלו-פרנקל: אם {% equation %}X{% endequation %} קיימת אז {% equation %}\bigcup X{% endequation %} קיימת.

כדי להבין למה האקסיומה הזו לא הופכת בניית קבוצות ל"תוכנית כבקשתך", בואו נראה למה אפילו היא לא מסייעת לי לבנות את {% equation %}\mathbb{N}{% endequation %} ואני עדיין צריך אקסיומה נפרדת עבור זה. כזכור, הצלחתי כבר לבנות את האיברים {% equation %}0,1,2,\dots{% endequation %} בנפרד, וכל האתגר הוא לאחד אותם לקבוצה אחת. אז רציתי לבנות את האיחוד {% equation %}\left\{ 0\right\} \cup\left\{ 1\right\} \cup\left\{ 2\right\} \cup\dots{% endequation %}. אקסיומת האיחוד מאפשרת לי לבנות איחוד אינסופי כזה, <strong>בתנאי אחד</strong>: שתהיה לי מלכתחילה קבוצה {% equation %}X{% endequation %} שמאגדת בתוכה את כל הקבוצות שאני מאחד. כלומר, אם הייתי מסוגל לבנות {% equation %}X{% endequation %} שמקיימת {% equation %}X=\left\{ \left\{ 0\right\} ,\left\{ 1\right\} ,\left\{ 2\right\} ,\dots\right\} {% endequation %} אז היה מתקיים {% equation %}\bigcup X=\mathbb{N}{% endequation %} כפי שרציתי. אבל אני <strong>לא יודע</strong> לבנות {% equation %}X{% endequation %} כזו בלי להיעזר באקסיומת האינסוף.

האם זו נקודה מבלבלת? בהחלט. הבשורות הטובות הן שלא תהיה נקודה עד כדי כך מבלבלת עד שנגיע לתורת הקבוצות האקסיומטית; הבלבול הזה הוא טעימה שמאפשרת לנו להרגיש <strong>עד כמה</strong> תורת הקבוצות האקסיומטית היא שדה מוקשים שהבנה שלו דורשת הבנה של ניואנסים עדינים מאוד.

עוד נקודה מבלבלת היא שלמעשה, אקסיומת האיחוד <strong>לא</strong> מוכיחה לבדה שאם {% equation %}A,B{% endequation %} קיימות אז {% equation %}A\cup B{% endequation %} קיימת. כדי לעשות את זה, צריך לעבור דרך הקבוצה {% equation %}X=\left\{ A,B\right\} {% endequation %}; אם {% equation %}X{% endequation %} קיימת אז {% equation %}\bigcup X=A\cup B{% endequation %} תהיה קיימת. לפני רגע הוכחתי שאם {% equation %}A,B{% endequation %} קיימות אז {% equation %}\left\{ A,B\right\} {% endequation %} קיימת בעזרת שילוב של אקסיומה 3 (שאמרה ש-{% equation %}\left\{ A\right\} {% endequation %} קיימת ו-{% equation %}\left\{ B\right\} {% endequation %} קיימת) ואקסיומה 4 (שאמרה ש-{% equation %}\left\{ A\right\} \cup\left\{ B\right\} {% endequation %} קיימת). אם אני "מחליש" את 4, אני צריך לחזק טיפה את 3 ולהרשות לה ליצור קבוצה עבור <strong>זוג</strong> איברים. לדבר הזה קוראים בצרמלו-פרנקל <strong>אקסיומת הזיווג</strong>: אם {% equation %}a,b{% endequation %} קיימים אז גם הקבוצה {% equation %}\left\{ a,b\right\} {% endequation %} קיימת. האקסיומה הקודמת נובעת ממנה בקלות: אם {% equation %}a=b{% endequation %} אז {% equation %}\left\{ a,b\right\} =\left\{ a,a\right\} =\left\{ a\right\} {% endequation %}, ולכן הטענה "אם {% equation %}a{% endequation %} קיים אז {% equation %}\left\{ a\right\} {% endequation %} קיימת" נובעת גם מהניסוח הזה של האקסיומה.

עכשיו בואו נעבור לחיתוך. כמו שהגדרתי "איחוד על קבוצה {% equation %}X{% endequation %}" כדרך להגדיר איחוד של אינסוף קבוצות בבת אחת כל עוד יש לנו "שליטה" עליהן שמתבטאת בכך שכולן יושבות באותה קבוצה {% equation %}X{% endequation %}, אני אגדיר גם חיתוך כזה בתור אוסף האיברים שנמצאים <strong>בכל</strong> איבר של {% equation %}X{% endequation %}, ואשתמש לצורך כך בסימן {% equation %}\forall{% endequation %} שמייצג "לכל". אם {% equation %}X\ne\emptyset{% endequation %} אז אני מגדיר

{% equation %}\bigcap X=\left\{ a\ |\ \forall A\in X:a\in A\right\} {% endequation %}

ההגדרה היא סבבה וסימטרית להגדרה של {% equation %}\bigcup X{% endequation %} והכל, אבל עולות ממנה שתי שאלות:

<ol> <li>מה מבטיח לנו ש-{% equation %}\bigcap X{% endequation %} קיימת?</li>


<li>למה דרשתי ש-{% equation %}X\ne\emptyset{% endequation %}?</li>

</ol>

בואו נענה על 1 קודם: שום דבר כרגע לא מבטיח לנו את זה. אנחנו צריכים עוד אקסיומה, שהיא הדבר החשוב ביותר שנדבר עליו בפוסט הזה. אחרי שנסיים איתה גם יהיה ברור יחסית למה {% equation %}X=\emptyset{% endequation %} הוא מקרה שאנחנו לא יכולים להרשות בשום פנים ואופן.

בואו נדבר לרגע על קבוצת <strong>המספרים הטבעיים הזוגיים</strong>, כלומר הקבוצה {% equation %}\left\{ 0,2,4,\dots\right\} {% endequation %}. זו ללא ספק קבוצה פשוטה וטבעית וכרגע אין לי מושג איך לבנות אותה. מכיוון שזו קבוצה אינסופית אני לא יכול ליצור אותה בעזרת אקסיומות הזיווג והאיחוד, בדיוק כפי שלא יכלתי ליצור את {% equation %}\mathbb{N}{% endequation %}. מצד שני, אקסיומת האינסוף שנותנת לי את {% equation %}\mathbb{N}{% endequation %} לא נותנת לי קבוצות אינסופיות אחרות. חסר לי משהו שיכול לייצר קבוצות אינסופיות "פשוטות יותר". עכשיו, האינטואיציה שתנחה אותי היא שאם כבר הצלחתי לבנות קבוצה {% equation %}A{% endequation %} ולא נגרמו מכך פרדוקסים, אז גם לקחת תת-קבוצה של {% equation %}A{% endequation %} לא הולך ליצור לי פרדוקסים - כלומר, שהקושי שלי יהיה ליצור קבוצות "גדולות מדי" ולא בגזירה של קבוצות קטנות יותר מתוך הקיימות. זו האינטואיציה שמאחורי האקסיומה עם הניסוח הכי מתירני עד כה, שבאופן לא מדויק אפשר לתאר בתור "אם {% equation %}A{% endequation %} קיימת אז כל תת-קבוצה שלה <strong>שאני יודע לתאר</strong> קיימת". ה"שאני יודע לתאר" הוא מילת המפתח כאן; אני לא אוכל להסביר פורמלית מה זה אומר עד שנגיע לתורת הקבוצות האקסיומטית, אבל זה בהחלט לא מרשה לי <strong>כל דבר</strong>.

בואו נתאר את קבוצת המספרים הזוגיים:

{% equation %}\left\{ n\in\mathbb{N}\ |\ \exists d\in\mathbb{N}:n=2d\right\} {% endequation %}

בהגדרה הזו יש שני מרכיבים: מה שמשמאל לקו המפריד ומה שמימין לו. מה שמשמאל הוא פשוט האמירה "אני בונה כרגע תת-קבוצה של {% equation %}\mathbb{N}{% endequation %}". כלומר, ה"עולם" שבו אני חי באותו הרגע הוא {% equation %}\mathbb{N}{% endequation %}, שאנחנו כבר יודעים שקיימת. מה שיש מימין לקו המפריד הוא <strong>קריטריון קונקרטי</strong> שמאפשר לי לקבוע מתי {% equation %}n{% endequation %} יהיה שייך לתת-הקבוצה שאני בונה ומתי לא. במקרה שלנו - אם {% equation %}n{% endequation %} ניתן לכתיבה בתור {% equation %}2d{% endequation %} כאשר {% equation %}d{% endequation %} הוא בעצמו איבר של {% equation %}\mathbb{N}{% endequation %}. האקסיומה שאתאר כרגע אומרת שאם הצלחתי להציג את תת-הקבוצה שלי בצורה הזו, אז היא קיימת. 

הנה ניסוח פורמלי: האקסיומה נקראת <strong>אקסיומת ההפרדה</strong> והיא אומרת שאם הקבוצה {% equation %}A{% endequation %} קיימת ואם {% equation %}\varphi{% endequation %} הוא קריטריון קונקרטי כלשהו שאיברים יכולים לקיים או לא לקיים, אז הקבוצה {% equation %}\left\{ a\in A\ |\ \varphi\left(a\right)\right\} {% endequation %} קיימת. כאן {% equation %}\varphi\left(a\right){% endequation %} זו דרך לומר "האיבר {% equation %}a{% endequation %} מקיים את הקריטריון {% equation %}\varphi{% endequation %}". אל תטרידו את עצמכם יותר מדי כרגע בשאלה מה זה קריטריון חוקי או לא - כלל האצבע הוא שהכל חוקי, ועל המקרים הנדירים שבהם זה לא נדבר הרבה, הרבה בהמשך.

נחזור עכשיו אל {% equation %}\bigcap X=\left\{ a\ |\ \forall A\in X:a\in A\right\} {% endequation %}. אם {% equation %}X\ne\emptyset{% endequation %} אז בפרט קיימת {% equation %}B\in X{% endequation %} כלשהי, ואפשר להשתמש ב-{% equation %}B{% endequation %} הזו בתור ה"עולם" שממנו גוזרים את {% equation %}\bigcap X{% endequation %}, באופן הבא:

{% equation %}\bigcap X=\left\{ a\in B\ |\ \forall A\in X:a\in A\right\} {% endequation %}

עכשיו כתבתי את {% equation %}\bigcap X{% endequation %} בצורה שאקסיומת ההפרדה מבקשת: בצד שמאל איבר ששייך לקבוצה שכבר ידוע שקיימת, ובאגף ימין קריטריון קונקרטי כלשהו. זה מוכיח את הקיום של {% equation %}\bigcap X{% endequation %} לכל מקרה למעט {% equation %}X=\emptyset{% endequation %}. ומה קורה במקרה הקצה הזה?

ובכן, יש לנו פה עוד סיטואציה של <strong>באופן ריק</strong>. אם {% equation %}X{% endequation %} ריקה, אז הקריטריון {% equation %}\forall A\in X:a\in A{% endequation %} מתקיים על ידי <strong>כל</strong> {% equation %}a{% endequation %}, כי הוא אף פעם לא "עומד למבחן". אם כן, {% equation %}\bigcap\emptyset{% endequation %} אמורה לצאת קבוצת "כל האיברים", אבל מה זה אומר, בעצם? כל האיברים <strong>איפה</strong>? אין לנו דרך לבנות קבוצה כזו; בקושי הצלחנו לבנות את {% equation %}\mathbb{N}{% endequation %}. למעשה, קל להוכיח שקבוצה כזו של "כל האיברים" (זה נקרא <strong>קבוצה אוניברסלית</strong>) לא קיימת: נניח שקבוצה {% equation %}U{% endequation %} של כל האיברים כן קיימת, אז בואו נגדיר את הקבוצה האהובה מהפרדוקס של ראסל: {% equation %}D=\left\{ A\in U\ |\ A\notin A\right\} {% endequation %}. הופס, קיבלנו קבוצה פרדוקסלית שאמורה להיות קיימת על פי אקסיומת ההפרדה (אגף ימין, {% equation %}A\notin A{% endequation %} הוא בהחלט קריטריון קונקרטי). לכן {% equation %}U{% endequation %} לא יכולה להתקיים, אם אנחנו רוצים לשמר את אקסיומת ההפרדה. מכאן ש-{% equation %}\bigcap\emptyset{% endequation %} זה פשוט ביטוי לא מוגדר.

נשארה לי אקסיומה אחת כדי שנוכל להתקדם הלאה עם "בואו נבנה בעזרת תורת הקבוצות את כל המתמטיקה". הססמא האהובה על באז לייטייר מ"צעצוע של סיפור" היא "לאינסוף... ומעבר לו!" וזה בדיוק מה שאנחנו עושים בתורת הקבוצות, בכמה מובנים שונים. גם כאן, באקסיומות, כבר הגענו אל האינסוף עם <strong>אקסיומת האינסוף</strong>, אבל זה לא מספיק - עדיין יש ביקום המתמטי אינספור קבוצות שאנחנו לא יכולים לבנות ובקושי דגדגנו את מה שכן מתעסקים בו. לדוגמא, את קבוצת המספרים הממשיים {% equation %}\mathbb{R}{% endequation %} לא נוכל לבנות עם האקסיומות שיש לנו עד עכשיו ותו לא. 

אפשר לחשוב על זה כך: ללא אקסיומת האינסוף, היינו משולים לחוקרת של היקום שנתקעה על כדור הארץ, בלי חללית ובלי כלום. כל היקום שלה מוגבל לכוכב לכת אחד וכדי להרחיב את אופקיה היא צריכה משהו <strong>חזק</strong> שיאפשר לה להימלט מבאר הכבידה של כדור הארץ. השיגור הזה אל החלל הוא מה שאקסיומת האינסוף נתנה לנו. עכשיו חוקרת היקום שלנו יכולה להסתובב לה בכיף במערכת השמש, לבקר בירח, להגיע אל מאדים, אולי אפילו לחבק את פלוטו ולומר לו שהוא כוכב לכת אמיתי; אבל מרחבי החלל האמיתיים עדיין לא נגישים לה. בשביל להגיע אליהם היא צריכה מנוע על-חלל. כדי להשלים את האנלוגיה, מנוע על-חלל הוא לא משהו שאפשר להשתמש בו אם נמצאים בתוך באר הכבידה של כוכב לכת - רק אחרי ההימלטות מכדור הארץ אפשר להשתמש בו. לכן שני השלבים של חקר היקום - הבריחה מכדור הארץ, והמעבר לכל יתר היקום - היו הכרחיים.

האקסיומה שתיתן לנו את מנוע העל-חלל נקראת <strong>אקסיומת קבוצת החזקה</strong>.

<strong>קבוצת החזקה</strong> של {% equation %}A{% endequation %} היא פשוט קבוצת כל תתי-הקבוצות של {% equation %}A{% endequation %}. פורמלית:

{% equation %}\mathcal{P}\left(A\right)\triangleq\left\{ B\ |\ B\subseteq A\right\} {% endequation %}

לדוגמא, אם {% equation %}A=\left\{ 1,2\right\} {% endequation %} אז {% equation %}\mathcal{P}\left(A\right)=\left\{ \emptyset,\left\{ 1\right\} ,\left\{ 2\right\} ,\left\{ 1,2\right\} \right\} {% endequation %}. באופן כללי אם ב-{% equation %}A{% endequation %} יש {% equation %}n{% endequation %} איברים אז ב-{% equation %}\mathcal{P}\left(A\right){% endequation %} יש {% equation %}2^{n}{% endequation %} איברים (תרגיל בקומבינטוריקה - להסביר למה) ולכן אני לא אכתוב עוד דוגמאות מפורשות כי זו פשוט הרבה כתיבה. אנחנו הולכים להתעסק כל כך הרבה עם קבוצות חזקה בהמשך שאני לא רואה סיבה להרחיב עליהן יותר מדי כרגע, אז אני אקפוץ ישר לאקסיומה: <strong>אקסיומת קבוצת החזקה</strong> פשוט אומרת שאם {% equation %}A{% endequation %} קיימת את {% equation %}\mathcal{P}\left(A\right){% endequation %} קיימת. זה, יחד עם שאר האקסיומות שיש לנו כרגע, מאפשר לנו לבנות יקום מתמטי כביר בגודלו, אבל לפרטים של הבניה הזו אכנס רק בשלב מאוחר בהרבה.

בואו נסכם את האקסיומות שראינו:

<ol> <li><strong>אקסיומת ההיקפיות</strong>: שתי קבוצות הן שוות אם הן בעלות אותם איברים: {% equation %}A=B{% endequation %} אם ורק אם {% equation %}a\in A\iff a\in B{% endequation %}.</li>


<li><strong>אקסיומת הקבוצה הריקה</strong>: הקבוצה {% equation %}\emptyset{% endequation %} קיימת.</li>


<li><strong>אקסיומת הזיווג</strong>: אם {% equation %}a,b{% endequation %} קיימים אז {% equation %}\left\{ a,b\right\} {% endequation %} קיימת.</li>


<li><strong>אקסיומת האיחוד</strong>: אם {% equation %}X{% endequation %} קיימת אז {% equation %}\bigcup X{% endequation %} קיימת.</li>


<li><strong>אקסיומת האינסוף: </strong>{% equation %}\mathbb{N}{% endequation %} קיימת.</li>


<li><strong>אקסיומת ההפרדה</strong>: אם {% equation %}A{% endequation %} קיימת ו-{% equation %}\varphi{% endequation %} הוא "קריטריון קונקרטי" אז {% equation %}\left\{ a\in A\ |\ \varphi\left(a\right)\right\} {% endequation %} קיימת.</li>


<li><strong>אקסיומת קבוצת החזקה</strong>: אם {% equation %}A{% endequation %} קיימת אז {% equation %}\mathcal{P}\left(A\right){% endequation %} קיימת.</li>

</ol>

זהו, זה מסיים את כל מה שרציתי לומר על צרמלו-פרנקל בשלב הזה. החל מהפוסט הבא גם נתחיל לעשות עם זה דברים מעניינים יותר מ"לנסות לבנות את קבוצת המספרים הטבעיים, להיכשל ואז להכריז שפשוט נוסיף אקסיומה מיוחדת בשביל זה". 