---
id: 2234
title: "הבעיה העשירית של הילברט - הפונקציה האקספוננציאלית היא דיופנטית"
date: 2012-11-12 21:11:31
layout: post
categories: 
  - תורת המספרים
tags: 
  - הבעיה העשירית של הילברט
  - טכני
  - פונקציות דיופנטיות
---
סוף סוף הגענו אל האקשן האמיתי. כזכור, עבור {% equation %}a>1{% endequation %} הגדרנו את משוואת פל {% equation %}x^{2}-dy^{2}=1{% endequation %} כאשר {% equation %}d=a^{2}-1{% endequation %}, וסימנו בתור {% equation %}x_{n}\left(a\right){% endequation %} את סדרת ערכי ה-{% equation %}x{% endequation %}-ים של פתרונות של המשוואה (כשכולם מוצגים בתור "חזקות" של הפתרון היסודי). המטרה שלנו כרגע היא להראות שהפונקציה {% equation %}f\left(a,k\right)=x_{k}\left(a\right){% endequation %} היא דיופנטית; לשם כך נציג מערכת משוואות שבה מככבים {% equation %}x,k,a{% endequation %} ועוד כל מני משתנים אחרים, כך שאחרי שמציבים ערכים קונקרטיים ב-{% equation %}x,k,a{% endequation %}, למערכת המשוואות שנותרה יש פתרון אם ורק אם {% equation %}x=x_{k}\left(a\right){% endequation %}. במערכת הזו יש שמונה משוואות. מוכנים? הנה הן:
<ol>
	<li>{% equation %}x^{2}-\left(a^{2}-1\right)y^{2}=1{% endequation %}</li>
	<li>{% equation %}u^{2}-\left(a^{2}-1\right)v^{2}=1{% endequation %}</li>
	<li>{% equation %}s^{2}-\left(b^{2}-1\right)t^{2}=1{% endequation %}</li>
	<li>{% equation %}v=ry^{2}{% endequation %}</li>
	<li>{% equation %}b=1+4py=a+qu{% endequation %}</li>
	<li>{% equation %}s=x+cu{% endequation %}</li>
	<li>{% equation %}t=k+4\left(d-1\right)y{% endequation %}</li>
	<li>{% equation %}y=k+e-1{% endequation %}</li>
</ol>
יפה. בואו נתחיל להבין מה המשמעות של כל זה ואיך כל משוואה עוזרת לנו.

נתחיל מהראשונה. כל פתרון של המשוואה הזו בעצם נותן לנו פתרון של משוואת פל עבור {% equation %}a{% endequation %} כלשהו. כלומר, כבר מהמשוואה הראשונה אנחנו יכולים להסיק שקיים {% equation %}i{% endequation %} כלשהו כך ש-{% equation %}x=x_{i}\left(a\right){% endequation %} וגם {% equation %}y=y_{i}\left(a\right){% endequation %}. בעצם כל האתגר שנותר לנו כעת הוא להוכיח ש-{% equation %}k=i{% endequation %} (זכרו! יש לחשוב על {% equation %}k{% endequation %} בתור קבוע - "פרמטר" שהצבנו במשוואות).

שתי המשוואות הבאות נותנות לנו עוד פתרונות למשוואות פל. משוואה 2 מראה לנו ש-{% equation %}u=x_{n}\left(a\right),v=x_{n}\left(a\right){% endequation %} עבור {% equation %}n{% endequation %} כלשהו; שימו לב שאלו הם איברים שונים באותה סדרה (של פתרונות משוואת פל עבור {% equation %}a{% endequation %}). לעומת זאת {% equation %}s=x_{j}\left(b\right),t=y_{j}\left(b\right){% endequation %} הם כבר פתרונות של משוואת פל שעשויה להיות שונה, תלוי אם {% equation %}b{% endequation %} שווה ל-{% equation %}a{% endequation %} או לא. לשם מה אנו נזקקים לעוד שני פתרונות? סבלנות.

מידע שאנחנו מקבלים מייד הוא ש-{% equation %}b{% endequation %} אכן שונה מ-{% equation %}a{% endequation %} ולמעשה הוא בהכרח גדול ממנו - זה נובע ממשוואה 5, {% equation %}b=a+qu{% endequation %}. זכרו שכל המשוואות הללו הן בשלמים <strong>חיוביים</strong> (זה פישוט שעשינו אי-אז בתחילת סדרת הפוסטים הזו).

כעת, האם אנחנו יכולים לומר משהו על הקשר שבין {% equation %}\left(x,y\right){% endequation %} ובין {% equation %}\left(u,v\right){% endequation %}? שניהם פתרונות של משוואת פל עם המקדם {% equation %}d=a^{2}-1{% endequation %}, אבל חוץ מזה הם כרוכים האחד בשני עם משוואה 4: {% equation %}v=ry^{2}{% endequation %}, או במפורש: {% equation %}y_{n}\left(a\right)=r\left(y_{i}\left(a\right)\right)^{2}{% endequation %}. במילים אחרות, {% equation %}\left(y_{i}\left(a\right)\right)^{2}{% endequation %} מחלק את {% equation %}y_{n}\left(a\right){% endequation %}. בפוסט הקודם הראינו שמכך נובע ש-{% equation %}y_{i}\left(a\right){% endequation %} מחלק את {% equation %}n{% endequation %} (וכמובן ש-{% equation %}i\le n{% endequation %}).

יפה, למדנו משהו על הקשר בין {% equation %}i{% endequation %} ו-{% equation %}n{% endequation %}. עכשיו בואו נכניס את {% equation %}x_{j}\left(b\right){% endequation %} לתמונה. משוואה 6, כשהיא מנוסחת בסימונים החדשים שלנו, אומרת ש-{% equation %}x_{j}\left(b\right)=x_{i}\left(a\right)+cx_{n}\left(a\right){% endequation %}. אפשר לסמן זאת גם כך: {% equation %}x_{j}\left(b\right)\equiv_{x_{n}\left(a\right)}x_{i}\left(a\right){% endequation %}. זה לא סוף מה שאפשר לעשות עם שקילות מודולו {% equation %}x_{n}\left(a\right){% endequation %}; משוואה 5 אומרת ש-{% equation %}b=a+qx_{n}\left(a\right){% endequation %}, כלומר {% equation %}b\equiv_{x_{n}\left(a\right)}a{% endequation %}.

עכשיו בואו נשלוף תוצאה מהפוסט הקודם: אם {% equation %}a\equiv_{c}b{% endequation %} אז לכל {% equation %}n{% endequation %} מתקיים ש-{% equation %}x_{n}\left(a\right)\equiv_{c}x_{n}\left(b\right){% endequation %} (זה נבע מההגדרה האינדוקטיבית של סדרות ה-{% equation %}x_{n}{% endequation %}-ים). אצלנו אפשר להסיק מזה ש-{% equation %}x_{j}\left(b\right)\equiv_{x_{n}\left(a\right)}x_{j}\left(a\right){% endequation %}, ולכן נקבל ש-{% equation %}x_{i}\left(a\right)\equiv_{x_{n}\left(a\right)}x_{j}\left(a\right){% endequation %}. לפי התוצאה מסוף הפוסט הקודם, המסקנה היא ש-{% equation %}j\equiv_{4n}\pm i{% endequation %}. כעת, מכיוון ש-{% equation %}y_{i}\left(a\right){% endequation %} מחלק את {% equation %}n{% endequation %}, הרי ש-{% equation %}4y_{i}\left(a\right){% endequation %} מחלק את {% equation %}4n{% endequation %} וכל דבר שמתחלק על ידו, ועל כן {% equation %}j\equiv_{4y_{i}\left(a\right)}\pm i{% endequation %}.

כעת בואו נשתמש שוב במשוואה 5, בחלק שלה שבו טרם השתמשנו שקובע ש-{% equation %}b=1+4py_{i}\left(a\right){% endequation %}, כלומר ש-{% equation %}b\equiv_{4y_{i}\left(a\right)}1{% endequation %}, כלומר ש-{% equation %}4y_{i}\left(a\right){% endequation %} מחלק את {% equation %}b-1{% endequation %}.

עכשיו בואו נשתמש בעוד תוצאה מהפוסט הקודם, לפיה {% equation %}y_{n}\left(a\right)\equiv_{a-1}n{% endequation %} (גם זה נבע די מייד מנוסחאות הנסיגה). אצלנו נשתמש בזה עם {% equation %}j{% endequation %} ונקבל ש-{% equation %}y_{j}\left(b\right)\equiv_{b-1}j{% endequation %}, כלומר {% equation %}y_{j}\left(b\right)\equiv_{4y_{i}\left(a\right)}j{% endequation %}. מבלבל? טיפה, כן. עכשיו כדי לבלבל עוד יותר נוסיף לתמונה את משוואה 7: {% equation %}y_{j}\left(b\right)=k+4\left(d-1\right)y_{i}\left(a\right){% endequation %} (<strong>שימו לב</strong> ש-{% equation %}d{% endequation %} כאן הוא משתנה בלי אילוצים עליו פרט לכך שיהיה חיובי; אנחנו <strong>לא</strong>יכולים להניח ש-{% equation %}d=a^{2}-1{% endequation %} וגם לא ניסינו לדרוש משהו כזה). מהמשוואה הזו נקבל מייד ש-{% equation %}y_{j}\left(b\right)\equiv_{4y_{i}\left(a\right)}k{% endequation %}, והנה הכנסנו את {% equation %}k{% endequation %} לתמונה סוף סוף. זכרו - מטרת העל שלנו היא להראות ש-{% equation %}k=i{% endequation %}, והתקדמנו יפה לקראת זה; בואו נערוך סיכום ביניים קצר של תוצאות שמצאנו:
<ol>
	<li>{% equation %}j\equiv_{4y_{i}\left(a\right)}\pm i{% endequation %}</li>
	<li>{% equation %}y_{j}\left(b\right)\equiv_{4y_{i}\left(a\right)}j{% endequation %}</li>
	<li>{% equation %}y_{j}\left(b\right)\equiv_{4y_{i}\left(a\right)}k{% endequation %}</li>
</ol>
משלושת אלו קיבלנו את השרשרת הבאה שבה כל השקילויות הן מודולו {% equation %}4y_{i}\left(a\right){% endequation %}: {% equation %}k\equiv y_{j}\left(b\right)\equiv j\equiv\pm i{% endequation %}. אם כן, עוד לא הוכחנו ש-{% equation %}k=i{% endequation %} אבל ראינו ש-{% equation %}k\equiv_{4y_{i}\left(a\right)}\pm i{% endequation %} וגם זו התחלה (וכמעט סיימנו!).

בואו נכניס לתמונה עכשיו את משוואה 8: {% equation %}y=k+e-1{% endequation %}. מה היא בעצם אומרת? זו בסך הכל הדרך הדיופנטית לכתוב {% equation %}k\le y_{i}\left(a\right){% endequation %} (כי {% equation %}e{% endequation %} הוא מספר חיובי כלשהו). כעת, בפוסט הקודם ראינו ש-{% equation %}i\le y_{i}\left(a\right){% endequation %}. אם תחשבו על זה קצת, זה אומר ש-{% equation %}k=i{% endequation %}! למה? כי {% equation %}k,i{% endequation %} שניהם נמצאים בתוך טווח שבו אין שני מספרים שונים ששקולים מודולו {% equation %}4y_{i}\left(a\right){% endequation %} - הטווח {% equation %}-2y_{i}\left(a\right)+1,\dots-1,0,1,\dots,2y_{i}\left(a\right){% endequation %} (זוכרים? דיברנו על זה קצת בפוסט הקודם). זהו, סיימנו את הכיוון הראשון! הראינו שאם נתון פתרון למשוואות הדיופנטיות עבור ערכים נתונים של {% equation %}x,k,a{% endequation %} אז הוא מקיים {% equation %}x=x_{k}\left(a\right){% endequation %}.

הכיוון השני הוא להראות שאם יש לנו ערכים נתונים של {% equation %}x,k,a{% endequation %} שמקיימים {% equation %}x=x_{k}\left(a\right){% endequation %} ואנחנו מציבים אותם במשוואות שלעיל, אז התוצאה היא מערכת משוואות פתירה. כלומר, אנחנו צריכים לקבוע מה יהיו הערכים ששאר המשתנים מקבלים ולהוכיח שכל המשוואות מתקיימות (עכשיו המשוואות הופכות להיות האויבים שלנו - אם קודם הן סיפקו לנו מידע, עכשיו הן מספקות לנו אילוצים שאנחנו חייבים לקיים).

בואו נתחיל ממשוואה 1 - היא קלה. אם {% equation %}x=x_{k}\left(a\right){% endequation %} אז אנחנו יודעים שיש {% equation %}y=y_{k}\left(a\right){% endequation %} כך ש-{% equation %}x^{2}+\left(a-1\right)y^{2}=1{% endequation %} מהגדרת משוואת פל. אז סיפקנו כבר את משוואה 1. בואו נעבור ל-2; כל פתרון אחר של משוואת פל עבור {% equation %}a{% endequation %} יספק אותה, אבל כדאי לבחור את הפתרון הזה בחוכמה כדי שגם שאר המשוואות יסופקו - נבחר {% equation %}m=2ky_{k}\left(a\right){% endequation %} (למה? כי זה עובד, כפי שנראה בהמשך) ונגדיר {% equation %}u=x_{m}\left(a\right){% endequation %} ו-{% equation %}v=y_{m}\left(a\right){% endequation %}, וזה כמובן שיספק את משוואה 2.

עכשיו, בפוסט הקודם ראינו ש-{% equation %}y_{n}{% endequation %} מחלק את {% equation %}y_{t}{% endequation %} אם ורק אם {% equation %}n{% endequation %} מחלק את {% equation %}t{% endequation %}, וכמו כן גם ראינו ש-{% equation %}y_{n}^{2}{% endequation %} תמיד מחלק את {% equation %}y_{ny_{n}}{% endequation %}. מהתוצאה השניה נובע ש-{% equation %}y_{k}^{2}{% endequation %} מחלק את {% equation %}y_{m/2}{% endequation %}, ומהראשונה נובע ש-{% equation %}y_{m/2}{% endequation %} מחלק את {% equation %}y_{m}{% endequation %} ולכן נקבל ש-{% equation %}y_{k}^{2}{% endequation %} מחלק את {% equation %}y_{m}{% endequation %}, כלומר {% equation %}y^{2}{% endequation %} מחלק את {% equation %}v{% endequation %}, כלומר יש {% equation %}r{% endequation %} כך ש-{% equation %}v=ry^{2}{% endequation %}, והנה סיפקנו את משוואה 4. זה עדיין לא מסביר עד הסוף את האופן שבו בחרנו את {% equation %}m{% endequation %} (אם כל מה שהיינו רוצים לעשות הוא להראות ש-{% equation %}y^{2}{% endequation %} מחלק את {% equation %}v{% endequation %} היה אפשר לבחור {% equation %}m=ky_{k}{% endequation %}) אבל זה הרווח הראשון שקצרנו מההגדרה הזו.

האתגר הבא, והגדול ביותר שלנו, הוא לספק את משוואה 5 שאיכשהו קושרת את הפרמטרים של כל שלוש משוואות פל שלנו יחד. נצטרך לבחור את {% equation %}b{% endequation %} בצורה חכמה מאוד, ועל פיו לבחור את מה שיפתור את משוואה 3. נתחיל דווקא מתכונה של {% equation %}u,v{% endequation %}: בפוסט הקודם ראינו שאם {% equation %}n{% endequation %} הוא זוגי אז {% equation %}y_{n}{% endequation %} הוא זוגי וכשהוא אי זוגי אז {% equation %}y_{n}{% endequation %} אי זוגי. במקרה שלנו בחרנו את {% equation %}m{% endequation %} בכוונה באופן שיבטיח שהוא זוגי ולכן {% equation %}v{% endequation %} זוגי, אבל זה אומר שבהכרח {% equation %}u{% endequation %} אי זוגי (כי {% equation %}u^{2}+\left(a^{2}-1\right)v^{2}=1{% endequation %}; מה תהיה הזוגיות של אגף שמאל אם גם {% equation %}u{% endequation %} וגם {% equation %}v{% endequation %} זוגיים?). אנחנו גם יודעים שהמחלק המשותף הגדול ביותר של {% equation %}u,v{% endequation %} הוא 1 (שוב, מהפוסט הקודם), ולכן גם המחלק המשותף הגדול ביותר של {% equation %}u{% endequation %} ושל {% equation %}4y{% endequation %} הוא 1. רגע, למה? ובכן, בואו נניח ש-{% equation %}p{% endequation %} הוא מספר גדול מ-1 שמחלק גם את {% equation %}u{% endequation %} וגם את {% equation %}4y{% endequation %}. אפשר תמיד להניח ש-{% equation %}p{% endequation %} ראשוני כי אם ניקח מחלק משותף כלשהו של {% equation %}u,4y{% endequation %} יהיה ראשוני שמחלק אותו; כמו כן, {% equation %}p{% endequation %} חייב להיות אי זוגי כי {% equation %}u{% endequation %} אי זוגי, ולכן {% equation %}p{% endequation %} לא מחלק את {% equation %}4{% endequation %}, ולכן כדי לחלק את {% equation %}4y{% endequation %} הוא חייב לחלק את {% equation %}y{% endequation %}. אבל ראינו ש-{% equation %}y{% endequation %} מחלק את {% equation %}v{% endequation %} ולכן קיבלנו ש-{% equation %}p{% endequation %} הוא מחלק משותף של {% equation %}u,v{% endequation %} וזו סתירה לכך שהם זרים.

איך זה עוזר לנו ש-{% equation %}u,4y{% endequation %} זרים? ובכן, זה מאפשר לנו לשלוף מהשרוול כלי נשק קטלני במיוחד. זכרו מהי משוואה 5 - בואו נכתוב אותה הפעם בתור זוג המשוואות שהיא:

{% equation %}b=1+4yp{% endequation %}

{% equation %}b=a+uq{% endequation %}

דרך אחרת, כמעט שקולה, לכתוב את מערכת המשוואות הזו היא:

{% equation %}b\equiv_{4y}1{% endequation %}

{% equation %}b\equiv_{u}a{% endequation %}

וזו מערכת משוואות מודולרית שבה המודולוסים הם זרים, מה שאומר ש<strong>משפט השאריות הסיני</strong> מבטיח שתמיד קיים לה פתרון. נבחר את הערך של המשתנה {% equation %}b{% endequation %} להיות הפתרון הזה. האם סיימנו? עוד לא, כי דרך הכתיבה המודולרית לא שקולה לחלוטין; היא הייתה שקולה רק אם {% equation %}p,q{% endequation %} היו יכולים להיות גם שליליים. למרבה המזל, אם {% equation %}b{% endequation %} הוא פתרון של מערכת המשוואות אז גם {% equation %}b+n\left(4yu\right){% endequation %} הוא כזה, לכל {% equation %}n{% endequation %} טבעי, ולכן תמיד אפשר לבחור {% equation %}b{% endequation %} גדול מספיק כדי ששתי המשוואות המקוריות יתקיימו. טראח! הנה סיפקנו גם את משוואה 5.

עכשיו, כשיש לנו את {% equation %}b{% endequation %} ביד, אפשר להגדיר את {% equation %}s,t{% endequation %} - הפתרונות למשוואה 3 - בתור {% equation %}s=x_{k}\left(b\right),t=y_{k}\left(b\right){% endequation %} (אותו {% equation %}k{% endequation %} כמו זה שהיה נתון לנו מלכתחילה). בפוסט הקודם ראינו שאם {% equation %}a\equiv_{c}b{% endequation %} אז {% equation %}x_{n}\left(a\right)\equiv_{c}x_{n}\left(b\right){% endequation %}. במקרה שלנו, {% equation %}b\equiv_{u}a{% endequation %} ולכן נקבל {% equation %}s\equiv_{u}x{% endequation %}, כלומר {% equation %}s=x+cu{% endequation %} בדיוק כמו משוואה 6. רגע, בדיוק? לא! מי מכם האמין לי? יש פה שוב את אותה בעיה כמו קודם - אף אחד לא ערב לנו ש-{% equation %}c{% endequation %} הזה הוא חיובי. כדי להיווכח בכך שהוא חיובי שימו לב לכך ש-{% equation %}b>a{% endequation %} (זה נובע מהמשוואה {% equation %}b=a+uq{% endequation %}). ולכן {% equation %}s=x_{k}\left(b\right)&gt;x_{k}\left(a\right)=x{% endequation %} (לא בטוחים בזה? הוכיחו לעצמכם, זה נובע מהגדרת {% equation %}x_{k}{% endequation %} כסדרת נסיגה).

נותרו רק משוואות 7 ו-8. משוואה 7 מתעסקת בקשר שבין {% equation %}t=y_{k}\left(b\right){% endequation %} ו-{% equation %}y=y_{k}\left(a\right){% endequation %} ו-{% equation %}k{% endequation %}. ראשית כל, שימו לב לכך ש-{% equation %}t\ge k{% endequation %} (בגלל שראינו בפוסט הקודם ש-{% equation %}y_{n}\ge n{% endequation %} תמיד). כמו כן, בפוסט הקודם ראינו גם ש-{% equation %}y_{n}\equiv_{a-1}n{% endequation %}, ובמקרה שלנו זה אומר ש-{% equation %}t\equiv_{b-1}k{% endequation %}. ממשוואה 5 ראינו ש-{% equation %}b=1+4yp{% endequation %} ולכן {% equation %}t\equiv_{4yp}k{% endequation %} ומכאן שבפרט {% equation %}t\equiv_{4y}k{% endequation %}. כעת, מה אומרת משוואה 7? ש-{% equation %}t=k+4\left(d-1\right)y{% endequation %}, ולכן העובדה ש-{% equation %}t\equiv_{4y}k{% endequation %} מראה את זה, כי כבר ראינו ש-{% equation %}t\ge k{% endequation %}.

נותרה רק משוואה 8: {% equation %}y=k+e-1{% endequation %}. להראות שהיא פתירה זה מיידי: {% equation %}y=y_{k}\left(a\right)\ge k{% endequation %} (מאוד שימושית, הטענה ש-{% equation %}y_{n}\left(a\right)\ge n{% endequation %}) ולכן קיים {% equation %}e{% endequation %} כנדרש ({% equation %}e=y-k+1{% endequation %}).

סיימנו! הוכחנו ש-{% equation %}f\left(k,a\right)=x_{k}\left(a\right){% endequation %} היא פונקציה דיופנטית! זה הישג לא מבוטל, עברנו דרך לא קצרה בדרך לחיסול הבעיה העשירית של הילברט.

לפני שאמשיך, אני רוצה לכתוב את משוואות 1-8 בצורה קצת יותר ידידותית למשתמש, עכשיו כשהבנו פחות או יותר מה הולך בהן:
<ol>
	<li>{% equation %}x,y{% endequation %} הם פתרונות של משוואת פל עם הפרמטר {% equation %}a{% endequation %}.</li>
	<li>{% equation %}u,v{% endequation %} הם פתרונות של משוואת פל עם הפרמטר {% equation %}a{% endequation %}.</li>
	<li>{% equation %}s,t{% endequation %} הם פתרונות של משוואת פל עם הפרמטר {% equation %}b{% endequation %}.</li>
	<li>{% equation %}y^{2}{% endequation %} מחלק את {% equation %}v{% endequation %}.</li>
	<li>{% equation %}b\equiv_{4y}1{% endequation %} וגם {% equation %}b\equiv_{u}a{% endequation %} וגם {% equation %}b>a{% endequation %}.</li>
	<li>{% equation %}s\equiv_{u}x{% endequation %} וגם {% equation %}s>x{% endequation %}.</li>
	<li>{% equation %}t\equiv_{4y}k{% endequation %} וגם {% equation %}t>k{% endequation %}.</li>
	<li>{% equation %}y\ge k{% endequation %}.</li>
</ol>
זה כבר נראה הרבה יותר אנושי. בעצם יש לנו כאן שלושה פתרונות למשוואות פל עם שני פרמטרים וכמה קשרים בסיסיים בין הפרמטרים. כל שאר המשתנים שהיו מעורבים במשוואות היו רק משתני עזר שסייעו לנו לכתוב באופן דיופנטי תכונות כמו {% equation %}\ge{% endequation %} וכמו שקילות מודולו. אני מציג את המשוואות כך כדי שיהיה קצת יותר קל להבין מאיפה הן הגיעו ומה עבר בראש של מי שהמציא אותן, למרות שאין לי מושג איך הגיעו להוכחה הזו.

עכשיו, קדימה לגביע הקדוש שלנו! נגדיר את הפונקציה {% equation %}h\left(n,k\right)=n^{k}{% endequation %} ונוכיח שהיא דיופנטית. לשם כך נבנה מערכת משוואות שכוללת את 8 המשוואות שהצגתי קודם, ועוד 4 משוואות חדשות:
<ol>
	<li>{% equation %}\left(x-y\left(a-n\right)-m\right)^{2}=\left(f-1\right)^{2}\left(2an-n^{2}-1\right)^{2}{% endequation %}</li>
	<li>{% equation %}m+g=2an-n^{2}-1{% endequation %}</li>
	<li>{% equation %}w=n+h=k+l{% endequation %}</li>
	<li>{% equation %}a^{2}-\left(w^{2}-1\right)\left(w-1\right)^{2}z^{2}=1{% endequation %}</li>
</ol>
זה הכל. למה זה עובד?

ובכן, בואו נניח ראשית כל שיש לנו פתרון למערכת המשוואות ונוכיח שמתקיים {% equation %}m=n^{k}{% endequation %}.

ראשית, שימו לב שמשוואה מס' 3 (החדשה; אם אתייחס למשוואות הישנות במספר שלהן אומר זאת במפורש מעתה) גוררת ש-{% equation %}w>1{% endequation %} (כי הוא סכום של שני מספרים חיוביים), ולכן {% equation %}\left(w^{2}-1\right)\left(w-1\right)^{2}z^{2}&gt;0{% endequation %} ומכאן על פי משוואה 4 ש-{% equation %}a>1{% endequation %}. אם {% equation %}a>1{% endequation %} אז כל המשוואות הישנות (1 עד 8) מראות ש-{% equation %}x=x_{k}\left(a\right){% endequation %} ו-{% equation %}y=y_{k}\left(a\right){% endequation %} - זה מה שעשינו קודם.

עכשיו, כולנו כבר הדחקנו את זה, אבל בפוסט הקודם ראינו ש-{% equation %}x_{k}\left(a\right)-y_{k}\left(a\right)\left(a-n\right)\equiv_{2an-n^{2}-1}n^{k}{% endequation %} (בחיי! אני לא ממציא את זה!). סוף סוף זה יועיל לנו קצת. כפי שאתם רואים, משוואה 1 מהונדסת פחות או יותר כדי להתאים לביטוי הזה; אם ניקח אותה מודולו {% equation %}\left(2an-n^{2}-1\right)^2{% endequation %}, נקבל:

{% equation %}\left(x-y\left(a-n\right)-m\right)^{2}\equiv_{\left(2an-n^{2}-1\right)^2}0{% endequation %}

ובגלל שבאופן כללי אם {% equation %}A^2|B^2{% endequation %} אז {% equation %}A|B{% endequation %} נקבל:

{% equation %}x-y\left(a-n\right)-m\equiv_{2an-n^{2}-1}0{% endequation %}

או במילים אחרות:

{% equation %}m\equiv_{2an-n^{2}-1}x-y\left(a-n\right)\equiv n^{k}{% endequation %} (המעבר האחרון נובע מהמשפט בפוסט הקודם).

יפה, אז אנחנו קרובים באופן מפתיע ליעד שלנו. רק צריך להשתכנע ש-{% equation %}m{% endequation %} ו-{% equation %}n^{k}{% endequation %} הם קטנים יותר מ-{% equation %}2an-n^{2}-1{% endequation %} ואז נסיים כמו קודם.

בואו תסתכלו רגע על משוואה 4. נראה לכם מוכר? זה לא במקרה, גם זו משוואת פל! הפעם {% equation %}w{% endequation %} הוא על תקן {% equation %}a{% endequation %}, ולכן יש {% equation %}j{% endequation %} כלשהו כך ש-{% equation %}a=x_{j}\left(w\right){% endequation %} ו-{% equation %}\left(w-1\right)z=y_{j}\left(w\right){% endequation %}. עכשיו, משפט מהפוסט הקודם שכבר השתמשנו בו כאן הוא ש-{% equation %}y_{j}\equiv_{w-1}j{% endequation %}, אבל מכיוון ש-{% equation %}y_{j}{% endequation %} מתחלק על ידי {% equation %}w-1{% endequation %} נובע מכך ש-{% equation %}j\equiv_{w-1}0{% endequation %}, ולכן בהכרח {% equation %}j\ge w-1{% endequation %}. עכשיו, אנחנו יודעים ש-{% equation %}x_{j}\left(w\right)\ge w^{j}{% endequation %} (שוב, פוסט קודם) ולכן {% equation %}a\ge w^{w-1}&gt;n^{k}{% endequation %}, כשהמעבר האחרון נובע מכך שמשוואה 2 מראה ש-{% equation %}w>a,k{% endequation %}. זה טוב מאוד - זה מראה ש-{% equation %}a{% endequation %} ענקי, כמו שאנחנו צריכים, אבל עוד לא סיימנו.

בואו נציץ במשוואה 2. מה שהיא בעצם אומרת הוא ש-{% equation %}m<2an-n^{2}-1{% endequation %} - כלומר, נותן לנו את הקוטן של {% equation %}m{% endequation %} שרצינו באופן מפורש. אז אם נראה ש-{% equation %}n^{k}&lt;2an-n^{2}-1{% endequation %}, נסיים את הכיוון הזה של ההוכחה. הדרך לעשות את זה היא להכניס טיפה אנליזה לתמונה. בואו נגדיר פונקציה {% equation %}f\left(n\right)=2an-n^{2}-1{% endequation %}. אז {% equation %}f\left(1\right)=2a-2\ge a{% endequation %} (אי השוויון האחרון נובע מכך ש-{% equation %}a>1{% endequation %}). כעת, נגזור את {% equation %}f{% endequation %} ונקבל {% equation %}f^{\prime}\left(n\right)=2a-2n{% endequation %} וזה גדול מ-0 לכל התחום {% equation %}1\le n<a{% endequation %}, כלומר {% equation %}f{% endequation %} היא פונקציה עולה בתחום הזה ולכן {% equation %}f\left(n\right)\ge a{% endequation %} לכל {% equation %}1\le n<a{% endequation %}. כעת, אם {% equation %}a>n^{k}{% endequation %} אז בפרט נקבל {% equation %}f\left(n\right)=2an-n^{2}-1\ge a&gt;n^{k}{% endequation %} (אין ל-{% equation %}n{% endequation %} ברירה, הוא חייב להיות קטן מ-{% equation %}a{% endequation %} אחרת {% equation %}n^{k}{% endequation %} לא היה קטן מ-{% equation %}a{% endequation %}). זה <strong>מסיים את הכיוון הראשון של ההוכחה</strong>!

נותר רק הכיוון השני - להראות שאם {% equation %}m=n^{k}{% endequation %}, אז יש למערכת המשוואות שלנו פתרון. בואו נתחיל ממשוואה 3. היא בסך הכל אומרת ש-{% equation %}w>n,k{% endequation %}, אז בואו נבחר את {% equation %}w{% endequation %} להיות מספר <strong>כלשהו</strong> שמקיים את זה. עכשיו, נגדיר {% equation %}a=x_{w-1}\left(w\right){% endequation %}. מה עם {% equation %}y_{w-1}\left(w\right){% endequation %}? מטענה מהפוסט הקודם שכבר עשינו בה שימוש פה, {% equation %}y_{w-1}\left(w\right)\equiv_{w-1}w-1\equiv0{% endequation %}. במילים אחרות, {% equation %}w-1{% endequation %} מחלק את {% equation %}y_{w-1}\left(w\right){% endequation %} ולכן {% equation %}y_{w-1}\left(w\right)=z\left(w-1\right){% endequation %}, והנה פתרנו את משוואה 4.

כעת, אם {% equation %}w>n{% endequation %} ו-{% equation %}w>k{% endequation %} אז {% equation %}a=x_{w-1}\left(w\right)\ge w^{w-1}&gt;n^{k}{% endequation %} ולכן נקבל (בדיוק כמו קודם) ש-{% equation %}m=n^{k}&lt;2an-n^{2}-1{% endequation %}, מה שנותן לנו פתרון למשוואה 2. נותרה רק משוואה 1!

ובכן, הבה ונגדיר {% equation %}x=x_{k}\left(a\right),y=y_{k}\left(a\right){% endequation %}. אנחנו יודעים ש-{% equation %}x_{k}\left(a\right)-y_{k}\left(a\right)\left(a-n\right)\equiv_{2an-n^{2}-1}n^{k}{% endequation %}, ובמילים אחרות: {% equation %}2an-n^{2}-1{% endequation %} מחלק את {% equation %}x-y\left(a-n\right)-m{% endequation %}, כלומר יש {% equation %}f{% endequation %} כך ש-{% equation %}x-y\left(a-n\right)-m=\left(f-1\right)\left({2an-n^{2}-1}\right){% endequation %}. רק שיש לנו בעיה קטנה - לא ברור אם {% equation %}f{% endequation %} הזה חיובי או שלילי בכלל. הפתרון הוא להעלות את שני אגפי המשוואה בריבוע, ואז לקבל {% equation %}\left(x-y\left(a-n\right)-m\right)^{2}=\left(f-1\right)^{2}\left({2an-n^{2}-1}\right)^{2}{% endequation %} וכעת אם {% equation %}f{% endequation %} היה שלילי אפשר להחליף אותו ב-{% equation %}\left|f\right|{% endequation %} מבלי לשים לב להבדל. זה מסיים עם משוואה 1, ומכיוון שכל המשוואות הישנות מסופקות על ידי הפתרון למשוואת פל {% equation %}x_{k}\left(a\right){% endequation %}, <strong>סיימנו את ההוכחה!</strong>

זה עדיין לא מוכיח שהבעיה העשירית של הילברט היא לא כריעה, אבל זה מוכיח שהפונקציה האקספוננציאלית היא דיופנטית - וזה המכשול שעמד בפני המתמטיקאים שעבדו על הבעיה במשך עשרות שנים. מכאן ואילך העניינים יפסיקו להיראות כמו "חשבון מכולת" ונחזור לדבר על התמונה הגדולה ולהבין איך פונקציה אקספוננציאלית עוזרת לנו.

קצת קרדיט לסיום על כל ההוכחה הזו. אני עובד, כאמור, על בסיס מאמר של מרטין דיוויס שקישרתי אליו בתחילת סדרת הפוסטים הזו. הוא מייחס את ההוכחה שהצגתי כאן (שמבחינה היסטורית אינה ההוכחה הראשונה מסוגה) לג'וליה רובינסון (אחת מהחוקרות המרכזיות של הבעיה העשירית) תוך שימוש בכמה מהרעיונות של יורי מאטיסייביץ' (מי שהוכיח לראשונה שיש פונקציה דיופנטית שגדלה אקספוננציאלית, ובכך סיים את ההוכחה של אי הכריעות של הבעיה העשירית). זו ההוכחה הפשוטה ביותר שהצלחתי למצוא; יש למאטיסייביץ' עצמו ספר על הבעיה, אבל את המאמר של דיוויס תמיד חיבבתי יותר.

