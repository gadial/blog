---
id: 2159
title: "הבעיה העשירית של הילברט - מבוא"
date: 2012-08-27 09:29:14
layout: post
categories: 
  - חישוביות
  - תורת המספרים
tags: 
  - בעיות לא כריעות
  - הבעיה העשירית של הילברט
  - הבעיות של הילברט
  - הילברט
  - משוואות דיופנטיות
---
בראשית ימי הבלוג <a href="http://www.gadial.net/2007/09/14/hilbert_tenth_problem_intro/">הזכרתי בפוסט</a> את הבעיה העשירית של הילברט, שהיא אחד מהנושאים המתמטיים החביבים עלי אישית, ומאז לא חזרתי לשם. הסיבה המרכזית הייתה שהתיאור המלא של פתרון הבעיה דורש גלישה לפרטים טכניים לא פשוטים כלל והעדפתי להימנע מזה (במילים אחרות - עצלנות); עם זאת, אני חושב שהגיע הזמן לנסות ולהתמודד עם האתגר הלא פשוט הזה. אל תיבהלו - לפני שנגיע לחלקים הטכניים יש לא מעט הסברים קלילים יחסית, שלדעתי הם מספקים מאוד למי שלא חש צורך להבין את הפתרון עד פרטיו הקטנים ביותר.

אני הולך להתבסס כאן בעיקר על האופן שבו הפרטים מוצגים במאמר הפנטסטי של מרטין דיוויס, Hilbert's Tenth Problem is Unsolvable, אבל קרוב לודאי שאחפף ואולי אציג דברים בצורה שונה.

נתחיל בהתחלה, עם הילברט. את הילברט הזכרתי כל כך הרבה פעמים בבלוג שנראה לי מוזר להציג אותו מחדש; הוא היה אחד מגדולי המתמטיקאים של כל הזמן, ובשנת 1900 היה הסופרסטאר הבלתי מעורער של עולם המתמטיקה; מתמטיקאי מגוון מאוד שאומרים עליו ששלט בכל תחומי המתמטיקה של זמנו. לכן, כשהוא נשא <a href="http://aleph0.clarku.edu/~djoyce/hilbert/problems.html">נאום</a> בקונגרס מתמטי שנערך בפריז בשנת 1900 ובו הציג רשימה של 23 בעיות מתמטיות שלדעתו העיסוק בהן יהיה פורה ומעניין, אנשים הקשיבו. על כל בעיה אפשר לכתוב פוסטים על גבי פוסטים, אבל אני הולך לדבר רק על הבעיה העשירית, כפי שודאי ניחשתם.

מה שהילברט אמר על הבעיה העשירית היא קצרצר - אחת מהשאלות שהוא דיבר עליהן ממש בחטף:
<blockquote>
<p dir="ltr">Given a diophantine equation with any number of unknown quantities and with rational integral numerical coefficients: to devise a process according to which it can be determined by a finite number of operations whether the equation is solvable in rational integers.</p>
</blockquote>
כמובן, יש כאן לא מעט מושגים שדורשים הבהרה. הכוכבת הראשית כאן היא <strong>המשוואה הדיופנטית</strong>. למרות השם המפחיד, זו בסך הכל משוואה פולינומית במספר משתנים, שמקדמיה שלמים. למשל, זו:

{% equation %}x+y=2{% endequation %}

זו משוואה עם שלל פתרונות, למשל {% equation %}x=y=1{% endequation %}. עוד פתרון הוא {% equation %}x=\frac{1}{2},y=\frac{3}{2}{% endequation %} ועוד פתרון הוא {% equation %}x=\pi,y=2-\pi{% endequation %}, אבל כשאנחנו מדברים על משוואות דיופנטיות אנחנו מתעניינים רק בפתרונות שהם <strong>מספרים שלמים</strong>, כלומר הפתרון הראשון לגיטימי, ושני האחרים לא. כך למשל למשוואה {% equation %}x^{2}=2{% endequation %} אין פתרון כלל, למרות ש-{% equation %}x=\sqrt{2}{% endequation %} מקיים את השוויון, וזה בגלל ש-{% equation %}\sqrt{2}{% endequation %} הוא לא מספר שלם (למי שתוהה למה הילברט אומר Rational Integers - זה כדי להבדיל אותם מ<strong>שלמים אלגבריים</strong> שהם הכללה של מספרים שלמים "רגילים" שצצה בתורת המספרים האלגברית, וזה לא רלוונטי לכל הדיון שלנו).

אם כן, הילברט מבקש איזה שהוא <strong>תהליך</strong> שמקבל משוואה כקלט, והפלט הוא תשובה לשאלה "האם יש למשוואה פתרון?". בימינו היינו משתמשים במילה "אלגוריתם" כדי לתאר "תהליך" שכזה (או, קונקרטית, "תוכנית מחשב"). על פניו, זה לא אמור להיות קשה במיוחד, לא?

ובכן, הבה ונתבונן במשוואה הבאה:

{% equation %}x^{3}+y^{3}=z^{3}{% endequation %}

למשוואה הזו יש כמה פתרונות ברורים - אלו שבהם {% equation %}x{% endequation %} או {% equation %}y{% endequation %} הם אפס, אבל בואו נתעלם מזה לשניה ונשאל את עצמנו אם יש לה <strong>עוד</strong> פתרונות בשלמים (לצורך העניין אפשר לדרוש שכל המשתנים יקבלו ערכים חיוביים ממש). התשובה היא לא; זה מקרה פרטי של <strong>המשפט האחרון של פרמה</strong>. לא יותר מדי קשה להוכיח שהתשובה היא לא, אבל <strong>זה דורש עבודה</strong>. ואז מגיעים למשוואה {% equation %}x^{5}+y^{5}=z^{5}{% endequation %} שדורשת עוד יותר עבודה; וכן הלאה וכן הלאה, ומשוואה כמו {% equation %}x^{37}+y^{37}=z^{37}{% endequation %} תדרוש <strong>המון</strong> עבודה, ובכל המקרים הללו סתם עבודה שחורה לא מספיקה - צריך יצירתיות וכושר דמיון כדי להתגבר על הבעיה. והמשוואות הללו הן <strong>מקרה פרטי פשוט</strong> של הבעיה הכללית שהילברט דיבר עליה... (שוב, אם מתעלמים מהפתרון הטריוויאלי של האפסים).

אוקיי, אז הבנו שהבעיה כנראה לא קלה. בואו נבין לרגע עד הסוף מה זו "משוואה פולינומית". יש לנו מספר כלשהו של משתנים, שאנחנו מסמנים בתור {% equation %}x,y,z{% endequation %} וכדומה (או בתור {% equation %}x_{1},x_{2},\dots,x_{n}{% endequation %} אם יש יותר מדי). מותר לנו לחבר אותם, לחסר אותם ולהכפיל אותם זה בזה ובעצמם, ואת כל זה אנחנו משווים בסוף לאפס. זה הכל. כך למשל {% equation %}x^2y^2-15=0{% endequation %} היא משוואה דיופנטית (חסרת פתרון) ו-{% equation %}x^2y^2-16=0{% endequation %} היא משוואה דיופנטית (עם הפתרון {% equation %}x=y=2{% endequation %}), וגם {% equation %}x^{5}y+17y^{3}z^{4}=16xyzw{% endequation %} היא משוואה דיופנטית (היא לא מושווה לאפס, אבל אפשר להעביר את ה-{% equation %}16xyzw{% endequation %} אגף). באופן פורמלי, אם {% equation %}p\left(x_{1},\dots,x_{n}\right){% endequation %} הוא פולינום כלשהו במשתנים {% equation %}x_{1},\dots,x_{n}{% endequation %}, אז הוא מגדיר את המשוואה הדיופנטית {% equation %}p\left(x_{1},\dots,x_{n}\right)=0{% endequation %}.

בואו נשחק קצת עם הגדרת הבעיה. למה לדבר רק על משוואה אחת? למה לא לדבר על <strong>מערכת</strong> של משוואות? למשל, המערכת הבאה:

{% equation %}x+y=8{% endequation %}

{% equation %}y+z=16{% endequation %}

שיש לה אינסוף פתרונות (למשל, {% equation %}x=8,y=0,z=16{% endequation %})? התשובה היא שאפשר, כי אפשר <strong>להמיר</strong> כל מערכת של מספר סופי של משוואות למשוואה יחידה. בואו נניח שיש לנו מערכת שהמשוואות בה מוגדרות על ידי הפולינומים {% equation %}p_{1},\dots,p_{k}{% endequation %} (אני לא כותב את המשתנים שלהם כדי לא לסרבל). אז הנה לכם משוואה אחת שיש לה פתרון <strong>אם ורק אם</strong> קיימת השמה לכל המשתנים שמאפסת בו זמנית את כל המשוואות:

{% equation %}p_{1}^{2}+p_{2}^{2}+\dots+p_{k}^{2}=0{% endequation %}

מה קורה כאן? יש לנו סכום של ריבועים. ריבועים של מספרים שלמים (והשמה של מספרים שלמים ב-{% equation %}p{% endequation %}-ים יכולה להחזיר רק מספרים שלמים) הם תמיד מספרים אי-שליליים; אם {% equation %}p_{i}\left(x_{1},\dots,x_{n}\right)\ne0{% endequation %} אז {% equation %}p_{i}^{2}\left(x_{1},\dots,x_{n}\right)&gt;0{% endequation %}, ולכן מספיק שאחת מהמשוואות לא תתאפס כדי שהביטוי {% equation %}p_{1}^{2}+p_{2}^{2}+\dots+p_{k}^{2}{% endequation %} כולו יהיה גדול מאפס. לכן מבחינתנו אין הבדל בין לפתור מערכת של משוואות דיופנטיות ובין לפתור אחת כזו, ונבחר את הניסוח שיותר נוח לנו כאשר נזדקק לו. אם לחדד - הוכחה שקיים אלגוריתם שפותר כל מערכת משוואות דיופנטית בוודאי תוכיח שקיים אלגוריתם שפותר כל משוואה כזו (כי משוואה היא מקרה פרטי של מערכת משוואות), אבל גם הוכחה שקיים אלגוריתם שפותר משוואה בודדת מראה שקיים אלגוריתם שפותר מערכת משוואות.

בואו נעבור לעוד פישוט, שהוא קצת יותר מחוכם. אני רוצה לטעון שאם יש אלגוריתם שבודק עבור משוואה דיופנטית אם יש לה פתרונות בשלמים כלשהם, אז יש אלגוריתם שבודק עבור משוואה דיופנטית אם יש לה פתרונות בשלמים <strong>חיוביים</strong> (גדולים מאפס). זה מטפל בבעיה של הפתרונות שכולם אפסים של המשוואות שקשורות למשפט האחרון של פרמה (למקרה שזה הפריע לכם).

מה התעלול? נניח ש-{% equation %}p\left(x_{1},\dots,x_{n}\right){% endequation %} היא משוואה שאנחנו רוצים לבדוק אם יש לה פתרון בשלמים חיוביים. אז נמיר אותה למשוואה המוזרה הבאה:

{% equation %}p\left(1+a_{1}^{2}+b_{1}^{2}+c_{1}^{2}+d_{1}^{2},\dots,1+a_{n}^{2}+b_{n}^{2}+c_{n}^{2}+d_{n}^{2}\right){% endequation %}

ונבדוק אם יש לה פתרון בשלמים <strong>בכלל</strong>.

מה קרה כאן? החלפנו כל משתנה {% equation %}x_{i}{% endequation %} בביטוי {% equation %}1+a_{i}^{2}+b_{i}^{2}+c_{i}^{2}+d_{i}^{2}{% endequation %} כאשר כל האותיות הללו הן משתנים. בבירור, מהנימוק שכבר נתתי כאן, כל הצבה אפשרית של ערכים במשתנים הללו תחזיר מספר חיובי ממש (1 ועוד מספר שהוא גדול או שווה לאפס). מצד שני, <strong>כל</strong> מספר טבעי חיובי יכול להתקבל כך; זו תוצאה לא טריוויאלית שנקראת "משפט ארבעת הריבועים של לגראנז'" ואני מקווה להוכיח יום אחד בבלוג (ההוכחה אינה קשה יותר מדי, והיא מהווה תירוץ טוב לדבר על קווטרניונים). אני חושב שהתעלול הזה מקסים למדי.

כעת, הבה ונעבור לסקירה קצרה ממעוף הציפור של מה שעלה בגורל הבעיה הזו.

במשך כמה עשרות שנים לא הייתה שום התקדמות ראויה לציון בנוגע לבעיה. זה לא מפתיע - כפי שכבר ראינו עם המשפט של פרמה, זו בעיה <strong>גדולה</strong>. אני לא בטוח על מה הילברט חשב לעצמו כשהוא הציב אותה. בינתיים, קרו כמה דברים במתמטיקה: קורט גדל הוכיח את משפטי אי השלמות שלו, וטיורינג (במקביל לצ'רץ') הוכיח שיש בעיות שאינן ניתנות לפתרון על ידי אף אלגוריתם, והעולם המתמטי הפך לבשל יותר להתמודדות עם הבעיה של הילברט. עכשיו היה אפשר לתת תיאור מתמטי פורמלי של אותו "תהליך" שהילברט ביקש, וגם היו כלים שמאפשרים להוכיח שהתהליך הזה לא קיים. מכיוון שכבר יש לי פוסטים על טיורינג ו<a href="http://www.gadial.net/2007/09/26/halting_problem/">בעיית העצירה</a> שלו לא אסביר כרגע איך מבצעים את הקסם המדהים הזה, להוכיח באופן ישיר שבעיה היא בלתי ניתנת לפתרון אלגוריתמי. זה למעשה לא חשוב, כי זה פתח את הדלת להוכחה <strong>עקיפה</strong> לכך שבעיות הן בלתי פתירות: די להוכיח ש<strong>אם</strong> הן פתירות, אז אפשר לפתור גם את הבעיות הבלתי פתירות של טיורינג.

בשנות ה-40 כבר היה ברור לכולם (כנראה; דיוויס מצטט במקום אחר את אמיל פוסט, אחד מגדולי העוסקים בתורת החישוביות, כאומר שהבעיה מזמינה הוכחת אי כריעות) שאין ולא יהיה אלגוריתם כמו שהילברט רצה, והשאלה הייתה רק איך להוכיח את זה. אז החלו לעסוק בבעיה מספר מתמטיקאים - מרטין דיוויס, ג'וליה רובינסון והילארי פטנאם. אחרי שהאבק שקע, אי שם בשנות השישים, כל מה שנותר היה להוכיח שקיימת משוואה אחת עם תכונות "חזקות" מסוימות שאסביר בהמשך. את ההוכחה הזו סיפק ב-1970 מתמטיקאי רוסי, יורי מאטיסביץ', ובכך חיסל את הבעיה - הוכח שלא קיים אלגוריתם שיודע להכריע לכל משוואה דיופנטית אם היא פתירה או לא, 70 שנים לאחר שהילברט שאל את השאלה.

האם הילברט טעה טעות מביכה כששאל את השאלה? בודאי שלא. ראשית, זו שאלה מרתקת והעיסוק בה היה מרתק; ושנית, קרוב לודאי שהילברט עצמו הרהר באפשרות שלא יהיה פתרון לבעיה. באותו נאום עצמו מ-1900 הוא מתייחס במפורש (לפני שהוא מציג את רשימת הבעיות שלו) לאפשרות שבעיה תהיה בלתי פתירה, ועל כן גם <strong>הוכחה לאי הפתירות שלה</strong> היא סוג משביע רצון של פתרון:
<blockquote>
<p dir="ltr">Occasionally it happens that we seek the solution under insufficient hypotheses or in an incorrect sense, and for this reason do not succeed. The problem then arises: to show the impossibility of the solution under the given hypotheses, or in the sense contemplated. Such proofs of impossibility were effected by the ancients, for instance when they showed that the ratio of the hypotenuse to the side of an isosceles right triangle is irrational. In later mathematics, the question as to the impossibility of certain solutions plays a preeminent part, and we perceive in this way that old and difficult problems, such as the proof of the axiom of parallels, the squaring of the circle, or the solution of equations of the fifth degree by radicals have finally found fully satisfactory and rigorous solutions, although in another sense than that originally intended. It is probably this important fact along with other philosophical reasons that gives rise to the conviction (which every mathematician shares, but which no one has as yet supported by a proof) that every definite mathematical problem must necessarily be susceptible of an exact settlement, either in the form of an actual answer to the question asked, or by the proof of the impossibility of its solution and therewith the necessary failure of all attempts.</p>
</blockquote>
אני חושב שהילברט היה מרוצה מגורל הבעיה שלו.

אם כן, הבה ונעבור לקצת יותר פרטים טכניים לגבי אופן ההוכחה. אנחנו עדיין נותרים בשטח ה"סקירתי" ברובו; בפוסטים הבאים ניכנס יותר לעובי הקורה.

הרעיון הראשון של דיוויס (ובאופן בלתי תלוי בו, רובינסון) היה לעבור לדבר על <strong>קבוצות דיופנטיות</strong>. בהינתן פולינום {% equation %}p\left(x_{1},\dots,x_{n},y_{1},\dots,y_{m}\right){% endequation %} שחילקנו את משתניו לשתי קבוצות, ה-{% equation %}x{% endequation %}-ים וה-{% equation %}y{% endequation %}-ים, אפשר להציב ערכים בתוך ה-{% equation %}x{% endequation %}-ים כדי לקבל פולינום חדש, {% equation %}q\left(y_{1},\dots,y_{m}\right)=p\left(a_{1},\dots,a_{n},y_{1},\dots,y_{m}\right){% endequation %}. עכשיו נשאל את השאלה - האם למשוואה הדיופנטית {% equation %}q\left(y_{1},\dots,y_{m}\right)=0{% endequation %} יש פתרון, או לא?

הקבוצה הדיופנטית ש-{% equation %}p{% endequation %} מגדיר היא הקבוצה של כל הערכים {% equation %}\left(a_{1},\dots,a_{n}\right){% endequation %} שאפשר להציב ב-{% equation %}x{% endequation %}-ים ולקבל משוואה דיופנטית פתירה. בכתיבה מתמטית פורמלית:

{% equation %}S_{p}=\left\{ \left(a_{1},\dots,a_{n}\right)\ |\ \exists\left(b_{1},\dots,b_{m}\right)p\left(a_{1},\dots,a_{n},b_{1},\dots,b_{m}\right)=0\right\} {% endequation %}

כאשר הערכים שה-{% equation %}a{% endequation %}-ים וה-{% equation %}b{% endequation %}-ים מקבלים הם מספרים טבעיים חיוביים. ברור לי שקצת קשה לעכל את ההגדרה הכללית הזו, אז בואו נראה כמה דוגמאות פשוטות.

דוגמה ראשונה היא <strong>קבוצת המספרים הפריקים</strong>. מספר הוא פריק אם אפשר להציג אותו כמכפלה של שני מספרים ששניהם קטנים ממנו (כשאני אומר "מספר" מכאן והלאה, אלא אם אני אומר אחרת במפורש, הכוונה היא למספר טבעי חיובי). הבה ונתבונן בפולינום הבא:

{% equation %}p\left(x,y_{1},y_{2}\right)=x-\left(1+y_{1}\right)\left(1+y_{2}\right){% endequation %}. נניח שהצבנו {% equation %}x=8{% endequation %}, אז נקבל את הפולינום {% equation %}p\left(8,y_{1},y_{2}\right)=8-\left(1+y_{1}\right)\left(1+y_{2}\right){% endequation %}. המשוואה הדיופנטית הזו פתירה על ידי ההשמה {% equation %}y_{1}=1,y_{2}=3{% endequation %} ולכן {% equation %}8\in S_{p}{% endequation %} במקרה הזה. לעומת זאת, אם נציב {% equation %}x=7{% endequation %} נקבל משוואה דיופנטית לא פתירה ולכן {% equation %}7\notin S_{p}{% endequation %} (תרגיל - למה {% equation %}\left(1+y_{1}\right)\left(1+y_{2}\right){% endequation %} ולא סתם {% equation %}y_{1}y_{2}{% endequation %}?)

במילים אחרות, אפשר <strong>להגדיר</strong> את קבוצת המספרים הפריקים באמצעות הפולינום {% equation %}p{% endequation %}. זה מצביע על הבעיה הכללית שתעניין אותנו - נתונה קבוצה של מספרים (או של זוגות/שלשות וכדומה של מספרים); האם קיים פולינום {% equation %}p{% endequation %} כך שהקבוצה שלנו שווה ל-{% equation %}S_{p}{% endequation %}? או במילים אחרות, האם הקבוצה הנתונה היא דיופנטית?

עוד דוגמה - יחס ה<strong>חלוקה</strong>. פורמלית, {% equation %}a{% endequation %} מחלק את {% equation %}b{% endequation %} אם קיים {% equation %}t{% endequation %} כך ש-{% equation %}at=b{% endequation %}, ומסמנים זאת {% equation %}a|b{% endequation %}. הפולינום {% equation %}p\left(x_{1},x_{2},y\right)=x_{2}-x_{1}y{% endequation %} מגדיר את הקבוצה {% equation %}\left\{ \left(x_{1},x_{2}\right)\ |\ x_{1}|x_{2}\right\} {% endequation %}, ולכן אנחנו אומרים שהוא מגדיר את יחס החלוקה (פורמלית, כך בדיוק יחס החלוקה מוגדר - קבוצת הזוגות אשר מקיימים את היחס).

נניח שהבנו את העקרון - מה עכשיו? ובכן, עכשיו נכנסת לתמונה תורת החישוביות. בתורת החישוביות גם כן מתעניינים בקבוצות של מספרים טבעיים; אמנם, בדרך כלל האובייקט שמדברים עליו הוא <strong>שפות</strong>, אבל אפשר באותה מידה לדבר גם על קבוצות של טבעיים בלי להגביל את כלליות הדיון. בהינתן קבוצה {% equation %}S{% endequation %} של טבעיים, המטרה של תורת החישוביות היא לבדוק אם קיים אלגוריתם שמכריע, בהינתן מספר טבעי {% equation %}a{% endequation %}, האם {% equation %}a\in S{% endequation %} או לא; ובדומה גם עבור קבוצות של {% equation %}n{% endequation %}-יות של טבעיים ({% equation %}n{% endequation %}-יה היא הכללה של זוג ושלשה - {% equation %}\left(a_{1},\dots,a_{n}\right){% endequation %}). אם יש אלגוריתם כזה אומרים ש-{% equation %}S{% endequation %} היא <strong>כריעה</strong> (או, מסיבה שתובהר בפוסטים הבאים, <strong>רקורסיבית</strong>).

לפעמים המצב הוא "חצי מוצלח" - יש אלגוריתם שעל קלט {% equation %}a{% endequation %} המקיים {% equation %}a\in S{% endequation %} יעצור ויגיד "כן! {% equation %}a\in S{% endequation %}!", אבל על קלט שמקיים {% equation %}a\notin S{% endequation %} הוא <strong>עשוי שלא לעצור</strong> (אם הוא עוצר, הוא צריך לומר במפורש "לא! {% equation %}a\notin S{% endequation %}"). קבוצה שקיים אלגוריתם כזה עבורה נקראת <strong>כריעה למחצה</strong> (או, מסיבה שתובהר בפוסטים הבאים, <strong>ניתנת למניה רקורסיבית</strong>).

יש קבוצות שהן כריעות (למשל, קבוצת הזוגיים), יש קבוצות שהן כריעות למחצה ויש קבוצות שהן לא כריעות בכלל. טיורינג נתן דוגמה לקבוצה שהיא כריעה למחצה אבל אינה כריעה; קבוצת כל המספרים שהם קידוד של מכונות טיורינג (למי שהמושג לא ברור לו, חשבו על תוכניות מחשב) שעוצרות על הקלט הריק (אני קצת משקר כאן - טיורינג לא בדיוק דיבר על זה - אבל מה זה חשוב). כאמור, לא ניכנס להסבר איך מוכיחים שהקבוצה הזו לא כריעה, אבל קל לראות שהיא כן כריעה למחצה: בהינתן מספר שמקודד מכונה, פשוט פענח את הקידוד (זה תמיד אפשרי - זו המהות של הקידוד של מכונות טיורינג) והריצו את המכונה על הקלט הריק. עצרה? יופי - עצרו גם אתם ודווחו שהקלט שייך לקבוצה. לא עצרה? לא נורא, במקרה הזה הקלט בודאות לא שייך לקבוצה ולכן זה לגיטימי לא לעצור.

כעת, ההוכחה שהבעיה העשירית של הילברט אינה כריעה ניתנת לתיאור כמורכבת משלוש טענות שמתחברות להן יחדיו:
<ol>
	<li>יש קבוצות כריעות למחצה שאינה כריעות.</li>
	<li>אם קיים אלגוריתם הפותר את הבעיה העשירית של הילברט, כל קבוצה דיופנטית היא כריעה.</li>
	<li>אוסף הקבוצות הדיופנטיות הוא <strong>בדיוק</strong> אוסף הקבוצות הכריעות למחצה.</li>
</ol>
את טענה 1 כבר תיארתי. טענה 2 ברורה למדי - נניח ש-{% equation %}S_{p}{% endequation %} היא קבוצה דיופנטית ואנחנו רוצים לבדוק האם {% equation %}\left(a_{1},\dots,a_{n}\right){% endequation %} שייך אליה. אז נציב את הערכים הללו ב-{% equation %}p{% endequation %}, נקבל משוואה דיופנטית, וכעת נפעיל את האלגוריתם הדמיוני של הילברט ונבדוק האם המשוואה הדיופנטית פתירה או לא. אם היא פתירה, נאמר ש-{% equation %}\left(a_{1},\dots,a_{n}\right)\in S{% endequation %} ואחרת נאמר ש-{% equation %}\left(a_{1},\dots,a_{n}\right)\notin S{% endequation %}. פשוט למדי, לא?

הטענה השלישית היא טענה כבדה וחזקה ביותר, והיא מה שארצה להוכיח בפוסטים הבאים. אדבר בהמשך גם על מקצת מההשלכות הנוספות שלה - פתרון הבעיה העשירית של הילברט הוא לא סוף הסיפור.

מדוע שלוש הטענות הללו סוגרות את הסיפור? שכן אם כל קבוצה כריעה למחצה היא דיופנטית, וכל קבוצה דיופנטית היא כריעה, אז המסקנה היא שכל קבוצה כריעה למחצה היא כריעה, וזה <strong>לא נכון</strong>. סתירה. לכן התנאים של 2 לא יכולים להתקיים, וזה סוף הסיפור (ליתר דיוק, זה מוכיח שלא קיים אלגוריתם שבודק עבור משוואה דיופנטית אם יש לה פתרונות בשלמים חיוביים, אבל כבר ראינו שמכך נובע שלא קיים גם אלגוריתם עבור הבעיה ה"כללית", כי אלגוריתם כזה היה מראה שהבעיה ה"פרטית" היא פתירה).

זהו, החלק הרעיוני הבסיסי תם - עכשיו כבר די ברור איך בערך פתרו את הבעיה; נותר רק להבין את הפרטים של שלב 3, והפרטים הללו הם מעניינים מאין כמותם, לטעמי, הגם שהם טכניים. יהיה כיף.
